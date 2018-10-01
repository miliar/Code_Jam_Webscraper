#!/usr/bin/env python

import sys

def split_arr(arr):
    if len(arr) < 2:
        return [arr]
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return [arr[:i], arr[i:]]
    return [arr]


def handle_case(case, end):

    arr = list(str(case))
    val = split_arr(arr)
    if len(val) == 1:
        converted_to_string = ''.join([str(x) for x in val[0]])
        return converted_to_string + end
    else:
        [left, right] = val
        converted_to_nines = ''.join(['9' for x in right])
        converted_to_num = int(''.join([str(x) for x in val[0]]))
        new_num = converted_to_num -1
        if new_num:
            return handle_case(new_num, converted_to_nines) + end
        else: 
            return converted_to_nines + end
    


with open(sys.argv[1], 'r') as my_file:
    first  = True
    num_lines = 0
    count = 1
    for line in my_file:
        if first:
            first = False
            num_lines = int(first)
        else :
            case = int(line)
            print('Case #%d: %s' % (count, str(handle_case(case, ''))))
            count = count + 1
