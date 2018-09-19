#!/usr/bin/env python2

import collections
import functools
import itertools
import math
from math import pi as pi
import multiprocessing
import operator
import profile
import sys

def read_int():
    return int(raw_input())

def read_ls():
    return [int(x) for x in raw_input().split()]

def run(r, t):
    paint = lambda x: (x+1)**2 - x**2
    cnt = 0
    p = paint(r)

    while p <= t:
        t -= p
        cnt += 1

        r += 2
        p = paint(r)

    return cnt

def main():
    for i in range(read_int()):
        result = run(*read_ls())

        # output
        print("Case #%d: %s" % (i+1, result))

if __name__ == "__main__":
    #profile.run('main()')
    sys.exit(main())
