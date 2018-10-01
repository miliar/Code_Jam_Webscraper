#!/usr/bin/env python

import sys

# Plan: 
# Create a list of gaps, and then for each person 
# determine the split, sort the gaps, and split the largest of the next one
#

def split (num):
    # if even return half twice, if odd return (x-1)/2 and (x-1)/2 + 1
    if (num % 2 == 0):
        half = num / 2
        return [half, half]
    else:
        half_lower = (num - 1) / 2
        return [half_lower, half_lower + 1]

def handle_case(case):
    [gap_len, num_people] = [int(x) for x in case.split(' ')]
    gap_list = [gap_len]
    last = num_people - 1
    for person in range(0, num_people):
        gap_list.sort()
        [gap1, gap2] = split(gap_list[-1] - 1)
        gap_list[-1] = gap1
        gap_list.append(gap2)
        if person == last:
            return '%d %d' % (gap2, gap1)
    return 'OOPS'


with open(sys.argv[1], 'r') as my_file:
    first  = True
    num_lines = 0
    count = 1
    for line in my_file:
        if first:
            first = False
            num_lines = int(first)
        else :
            case = line
            print('Case #%d: %s' % (count, str(handle_case(case))))
            count = count + 1
