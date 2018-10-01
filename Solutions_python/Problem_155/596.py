#! /usr/bin/env python3

import sys

number_of_test_cases = int(sys.stdin.readline())

for test_no in range(1, number_of_test_cases+1):
    Friends=0
    ovating=1
    for c in sys.stdin.readline().split()[1]:
        if ovating>0:
            ovating -= 1
        else:
            Friends += 1
        ovating += int(c)
    print("Case #{}: {}".format(test_no, Friends))

