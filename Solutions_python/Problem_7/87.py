#!/usr/bin/env python

import sys
import math
from xpermutations import *

try:
    import psyco
    psyco.full()
except ImportError:
    print("Try using psyco for better performance")


def solve():
    f = open(sys.argv[1])
    N = int(f.readline())
    for nn in range(N):
        n, A, B, C, D, x0, y0, M = map(int, f.readline().split(" ")) 
        list1 = []
        X = x0
        Y = y0
        list1.append((X, Y))
        for i in range(n - 1):
            X = (A * X + B) % M
            Y = (C * Y + D) % M
            list1.append((X, Y))

        res = 0
        for comb in xuniqueCombinations(list1, 3):
            if isvalid(comb):
                res += 1

        print("Case #%i: %i" % (nn + 1, res))


def isvalid(triangle):
    x1, y1 = triangle[0]
    x2, y2 = triangle[1]
    x3, y3 = triangle[2]
    x = (x1 + x2 + x3) / 3.0
    y = (y1 + y2 + y3) / 3.0
    if x - math.floor(x) == 0.0 and y - math.floor(y) == 0.0:
        return True
    else:
        return False
    
solve()
