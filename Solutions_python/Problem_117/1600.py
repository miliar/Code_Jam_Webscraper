#! /usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

input_filename = 'B-small-attempt0.in'
output_filename = 'B-small-attempt0.out'

def possible_pattern(lawn):
    for position, height in ndenumerate(lawn):
        row = lawn[position[0],:]
        column = lawn[:,position[1]]
        if sum(row) > height*len(row) and sum(column) > height*len(column):
            return False
    return True

f = open(input_filename)

no_test_cases = None
lawns_dims = []
lawns = []
current_test_case = -1
current_lawn = []

for line in f:
    if no_test_cases == None:
        no_test_cases = int(line)
        continue
    if current_test_case < 0:
        lawns_dims.append(map(int, line.split()))
        current_test_case = abs(current_test_case)
        continue
    if len(current_lawn) < lawns_dims[current_test_case-1][0]-1:
        current_lawn.append(map(int, line.split()))
        continue
    else:
        current_lawn.append(map(int, line.split()))
        lawns.append(array(current_lawn))
        current_lawn = []
        current_test_case = -abs(current_test_case)-1

f.close()

f = open(output_filename, 'a')

for i in range(no_test_cases):
    f.write('Case #'+str(i+1)+': ')
    if possible_pattern(lawns[i]):
        f.write('YES\n')
    else:
        f.write('NO\n')

f.close()
