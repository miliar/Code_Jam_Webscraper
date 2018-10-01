#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

fin = open("d:/google/A-small-attempt0.in")
fout = open("d:/google/A-small-attempt0.out", "w")
num_test_cases = fin.readline()
BAD = "Bad magician!"
CHEATED = "Volunteer cheated!"
result_list = []
for i in xrange(1, int(num_test_cases) + 1):
    guess = []
    case_num = "Case #%d: "%i
    for try_times in xrange(2):
	num_hint = fin.readline()
	for row_num in xrange(1, 5):
	    row_numbers = fin.readline()
	    if int(num_hint) == row_num:
		guess.append(set(row_numbers.strip().split(' ')))
    result = guess[0] & guess[1]
    if len(result) == 0:
	result_list.append(case_num + CHEATED)
    elif len(result) > 1:
	result_list.append(case_num + BAD)
    else:
	result_list.append(case_num + result.pop())
fout.writelines('\n'.join(result_list))
	

