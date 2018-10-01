#!/usr/bin/env python

import sys
# import string

# file_name = 'Sample.in'
# file_name = 'A-small-practice.in'
# file_name = 'A-small-attempt0.in'
file_name = 'A-large.in'

# open input file
try:
    with open(file_name, 'r') as f:
        num_cases = int(f.readline())
        in_lines = [i.strip('\n') for i in f.readlines()]
except EnvironmentError:
    print "Can't open input file!"
    sys.exit(-1)
# from pprint import pprint
# print num_cases
# pprint(in_lines)

if 'Sample.in' == file_name:
    try:
        with open('Sample.out', 'r') as f:
            sample_out_lines = [i.strip('\n') for i in f.readlines()]
    except:
        print "Can't open sample output file"
        sys.exit(-2)
    # need to test smaple output later


# process the input file
test_cases = []
one_case = []
for lin in in_lines:
    if lin != '':
        one_case.append(tuple(lin))
    else:
        test_cases.append(tuple(one_case))
        one_case = []
test_cases = tuple(test_cases)
# from pprint import pprint
# pprint(test_cases)


def check(four):
    if '.' in four:
        return None

    if 'T' not in four:
        if four[0] == four[1] == four[2] == four[3]:
            return four[0] + ' won'
    else:
        four.remove('T')
        three = four
        if three[0] == three[1] == three[2]:
            return three[0] + ' won'

    return None


def result(one_case):
    for i in range(4):
        to_check = [
                one_case[i][0],
                one_case[i][1],
                one_case[i][2],
                one_case[i][3]
        ]
        res = check(to_check)
        if res is not None:
            return res
    for i in range(4):
        to_check = [
                one_case[0][i],
                one_case[1][i],
                one_case[2][i],
                one_case[3][i]
        ]
        res = check(to_check)
        if res is not None:
            return res
    to_check = [
            one_case[0][0],
            one_case[1][1],
            one_case[2][2],
            one_case[3][3]
    ]
    res = check(to_check)
    # print to_check, res
    if res is not None:
        return res
    to_check = [
            one_case[3][0],
            one_case[2][1],
            one_case[1][2],
            one_case[0][3]
    ]
    res = check(to_check)
    if res is not None:
        return res

    for i in range(4):
        if '.' in one_case[i]:
            return 'Game has not completed'
    return 'Draw'


out_lines = []
for i in range(num_cases):
    lin = 'Case #' + str(i + 1) + ': '
    lin += result(test_cases[i])
    out_lines.append(lin)
    print lin
# from pprint import pprint
# pprint(out_lines)

# test sample output
if 'Sample.in' == file_name:
    assert str(out_lines) == str(sample_out_lines)
