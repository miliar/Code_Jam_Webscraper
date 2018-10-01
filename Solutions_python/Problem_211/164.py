#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Round 1C - Problem C
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys
from math import pi


def get_mins(units):

    vals = {u for u in units}

    s = sorted(vals)

    if len(s) == 1:
        return s[0], s[0]
    else:
        return s[0], s[1]


def solve(N, K, U, units):
    """  Solve the problem """

    if N == 1:
        return min(1.0, units[0] + U)

    while U > 0.0:
        low, llow = get_mins(units)

        if low == llow:
            # all units have the same value
            add = U / N
            units = [low + add] * N
            U = 0.0
        else:
            # count how many units are at the minimum
            count = sum([1 for u in units if u == low])

            # add U until both are equal.. and iterate
            cost = (llow - low) * count
            real = min(U, cost)
            U -= real

            partial = real / count
            for i in range(N):
                if units[i] < llow:
                    units[i] += partial

    prob = 1.0
    for u in units:
        prob *= min(u, 1.0)

    return max(prob, 0.0000001)


input_path = sys.argv[1]

with open(input_path) as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):
        N, K = list(map(int, input_file.readline().strip().split()))
        U = float(input_file.readline().strip())
        units = list(map(float, input_file.readline().strip().split()))

        solution = solve(N, K, U, units)
        print('Case #{0}: {1}'.format(case, solution))
