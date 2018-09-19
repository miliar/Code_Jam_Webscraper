#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys, math
from decimal import Decimal, getcontext, ROUND_CEILING

getcontext().prec=51
getcontext().rounding = ROUND_CEILING


def solve(t):
    gaps = []
    for i in range(len(t)-1):
        gaps.append(abs(t[i] - t[i+1]))
    common = denoms(gaps)
    return ((Decimal(min(t))/common).to_integral_exact() * common) - min(t)


def main(argv=sys.argv[1:]):
    fin = open(argv[0], 'r')
    fout = open(argv[1], 'w')
    
    count = int(fin.readline().strip())
    for index in range(count):
        t = [int(i) for i in fin.readline().strip().split()][1:]
        result = solve(t)
        print 'Case #%d: %d' % (index+1, result)
        print >>fout, 'Case #%d: %d' % (index+1, result)


def denoms(nums):
    def euclid(numA, numB):
        while numB != 0:
            numB, numA = numA % numB, numB
        return numA
    return reduce(euclid, nums)


def test(x):
    for i in range(x):
        solve([800000000000000000000000000000000000000001, 900000000000000000000000000000000000000001])
        print '%d/%d' % (i, x)

if __name__ == '__main__':
    main()