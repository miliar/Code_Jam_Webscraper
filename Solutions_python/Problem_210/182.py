#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Round 1C - Problem B
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys
from math import pi



def solve(C, D, clist, dlist):
    """  Solve the problem """

    if C + D < 2:
        return 2

    if C == 1 and D == 1:
        return 2

    if C == 2:
        true_list = clist
    else:
        true_list = dlist

    if true_list[0][0] > true_list[1][0]:
        first = true_list[1]
        last = true_list[0]
    else:
        first = true_list[0]
        last = true_list[1]

    if (last[0] - first[1]) >= 720:
        return 2

    if (first[0] + (1440 - last[1])) >= 720:
        return 2

    return 4



input_path = sys.argv[1]

with open(input_path) as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):
        C, D = list(map(int, input_file.readline().strip().split()))

        clist = []

        for _ in range(C):
            act = list(map(int, input_file.readline().strip().split()))
            clist.append(act)

        dlist = []
        for _ in range(D):
            act = list(map(int, input_file.readline().strip().split()))
            dlist.append(act)

        solution = solve(C, D, clist, dlist)
        print('Case #{0}: {1}'.format(case, solution))
