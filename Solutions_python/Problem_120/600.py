#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem A. Bullseye
# https://code.google.com/codejam/contest/2418487/dashboard#s=p0
#

import sys
import itertools


def solve(r, t):
    count = 0
    paint = (r + 1) ** 2 - r ** 2
    while t >= paint:
        count += 1
        t -= paint
        r += 2
        paint = (r + 1) ** 2 - r ** 2
    return count

# (2**2 - 1**2) + (4**2 - 3**2) + (6**2 - 5**2) + (8**2 - 7**2)
# ↓
# (2-1) * (2+1) + (4-3) * (4+3) + (6-5) * (6+5) + (8-7) * (8+7)

def solve(r, t):
    count = 0
    paint = (r + 1) + r
    while t >= paint:
        count += 1
        t -= paint
        r += 2
        paint = (r + 1) + r
    return count


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        r, t = map(int, IN.readline().split())
        OUT.write('Case #%d: %d\n' % (index + 1, solve(r, t)))


def makesample(rmax=1000, tmax=1000, T=1000):
    import random
    print T
    for index in range(T):
        r = random.randint(1, rmax)
        t = random.randint(1, tmax)
        print r, t


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)

