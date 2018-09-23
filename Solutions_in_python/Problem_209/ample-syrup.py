#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import itertools
# from decimal import Decimal

def solve(t, k):
    scores = []
    # max = 0.0
    # max_radi = 0.0
    for (r, h) in t:
        radi_area = r ** 2 * math.pi
        height_area = 2 * math.pi * r * h
        # curr_max = radi_area + height_area
        # if curr_max > max:
        #     max_radi = radi_area
        scores.append((radi_area, height_area))

    all_possible = itertools.permutations(scores)
    max_result = 0
    for s in all_possible:
        result = sum(s[0])
        for i in range(1, k):
            r, h = s[i]
            result += h
        if result > max_result:
            max_result = result

    return max_result

outf = open("ample-syrup.out","w")
inf = open("A-small-attempt1.in", "r")

t = int(inf.readline())
for i in range(0, t):
    n, k = map(int, inf.readline().split(" "))
    test_case = []
    for y in range(0, n):
        test_case.append(map(float, inf.readline().split(" ")))
    res = solve(test_case, k)
    outf.write("Case #{0}: {1}\n".format(i+1, res))

outf.close()
inf.close()
