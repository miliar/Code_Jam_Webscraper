# Where is the first bad number at?
def get_broken_index(nums_str):
    current = nums_str[0]
    for i, num in enumerate(nums_str):
        if int(current) > int(num):
            return i
        current = num
    return False


def fix_broke_index(nums_str, index):
    nums_str = [int(x) for x in nums_str]
    nums_str[index-1] -= 1
    # set it to all nines after the broken point
    nums_str[index:] = [9] * len(nums_str[index:])
    return [str(x) for x in nums_str]


def convert_str_list_to_int(str_list):
    return int(''.join(str_list))


# --------------  START HERE  ---------------
def get_next_tidy(num):
    nums_str = list(str(num))
    # Get the first bad spot
    broke_index = get_broken_index(nums_str)
    if not broke_index:
        return convert_str_list_to_int(nums_str)
    fixed = fix_broke_index(nums_str, broke_index)
    # Make sure we really fixed it
    return get_next_tidy(convert_str_list_to_int(fixed))
        

with open('text.txt') as f:
    text = [x.strip() for x in f.readlines()][1:]
    print(text)

output = []
for i, val in enumerate(text):
    output += ["Case #{}: ".format(i+1) + str(get_next_tidy(int(val)))]

print(output)

with open('output.txt', 'w+') as f:
    f.write('\n'.join([str(x) for x in output]))
