#!/usr/bin/env python
# encoding: utf-8
"""
FreeCell.py

Created by Graham Dennis on 2011-05-21.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys

def greatestCommonFactor(a, b):
    if a < b:
        a, b = b, a
    while a - b:
        c = a - b
        a = max(b, c)
        b = min(b, c)
    return a

def leastCommonMultiple(a, b):
    return (a * b) / greatestCommonFactor(a, b)

def solve(p):
    if p == 0:
        return 1, 0, 1
    lcm = leastCommonMultiple(100, p)
    played = lcm/p
    won = lcm/100
    lost = played - won
    return played, won, lost

def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    for t in xrange(T):
        N, PD, PG = map(int, f.readline().split())
        D, WD, LD = solve(PD)
        G, WG, LG = solve(PG)
        if D <= N and (WG > 0 or WG == WD) and (LG > 0 or LG == LD):
            state = "Possible"
        else:
            state = "Broken"
        # print lcmD, lcmG, D, G
        print "Case #%i: %s" % (t+1, state)

if __name__ == "__main__":
    sys.exit(main())
