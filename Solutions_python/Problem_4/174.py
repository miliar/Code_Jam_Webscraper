#!/usr/bin/env python

import sys

try:
    import psyco
    psyco.full()
except ImportError:
    print("Try using psyco for better performance")


def solve():
    f = open(sys.argv[1])
    T = int(f.readline())
    for t in range(T):
        n = int(f.readline())
        input1 = map(int, f.readline().split(" "))
        input2 = map(int, f.readline().split(" "))
        res = mult(list(sorted(input1)), list(reversed(sorted(input2))))
        print("Case #%i: %i" % (t + 1, res))

def mult(per1, per2):
    res = 0
    for n in range(len(per1)):
        res += per1[n] * per2[n]
    return res

solve()
