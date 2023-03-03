# %%
#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list

# %%
def contains_odd(input_list):
    i = 0
    while(i < len(input_list) and input_list[i] % 2 == 0):
        i += 1
    if(i < len(input_list)):
        return True
    return False

# %%
#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list

# %%
def is_odd(input_list):
    outlist = []
    for x in input_list:
        if (x % 2 != 0):
            outlist.append(True)
        else:
            outlist.append(False)
    return outlist

# %%

#Create a function that accpects 2 lists of integers and returns their element wise sum. <br>
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

# %%
def element_wise_sum(input_list_1, input_list_2):
    i = 0
    outlist = []
    while (i < len(input_list_1) or i < len(input_list_2)):
        outlist.append(input_list_1[i] + input_list_2[i])
        i += 1
    return outlist

# %%
#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict

# %%
def dict_to_list(input_dict):
    outlist=[]
    for key,value in input_dict.items():
        outlist.append((key,value))
    return outlist

# def dict_to_list(input_dict):
#     return input_dict.items()

# %%
#If all the functions are created convert this notebook into a .py file and push to your repo


