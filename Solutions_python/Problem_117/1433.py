#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Description"""

__author__ = 'Pedro Larroy'
__version__ = '0.1'

import os
import sys
import copy
import pprint
pp = pprint.PrettyPrinter(indent=4)


def readcase(fd):
    (N,M) = map(int, fd.readline().rstrip().split())
    Lr = []
    Lc = []
    for i in range(N):
        Lr.append(map(int, fd.readline().rstrip().split()))
        assert(len(Lr[-1]) == M)

    for i in range(M):
        col = []
        for row in Lr:
            col.append(row[i])
        Lc.append(col)

    case = {"N":N,
        "M":M,
        "Lr": Lr,
        "Lc": Lc
        }
    return case

def read_input(fname):
    fd = open(fname, 'rb')
    ncases = int(fd.readline().rstrip())
    cases = []
    for i in range(ncases):
        cases.append(readcase(fd))
    return cases


def solve(case):
    MAX = 1
    MIN = 0
    row_min_max = []
    col_min_max = []
    for row in case["Lr"]:
        row_min_max.append((min(row), max(row)))

    for col in case["Lc"]:
        col_min_max.append((min(col), max(col)))

    for (rowi, row) in enumerate(case["Lr"]):
        for (coli, x) in enumerate(row):
            if x < row_min_max[rowi][MAX] and x < col_min_max[coli][MAX]:
                #print 'x',x
                #print 'rowi', rowi, 'coli', coli
                #pp.pprint(row_min_max)
                #pp.pprint(col_min_max)
                return 'NO'
    return 'YES'

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    fname = sys.argv[1]
    cases = read_input(fname)
    #pp.pprint(cases)
    for (i, case) in enumerate(cases):
        print 'Case #{0}: {1}'.format(i+1, solve(case))

    return 1

if __name__ == '__main__':
    sys.exit(main())

