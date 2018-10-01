#! /usr/bin/python2

import sys
from itertools import *

def badd(x, y):
    diff = 2*(x & y)
    return (x+y)-diff

def bsum(l):
    return reduce(badd, l)

def valid_piles(p1, p2):
    return True if bsum(p1) == bsum(p2) else False

def solve(candy, casenum):
    res = 0
    found = False
    keys = list(range(len(candy)))
    for i in xrange(1, len(keys)):
        for s in combinations(keys, i):
            rem = set(keys) - set(s)
            p1 = map(lambda k: candy[k], s)
            p2 = map(lambda k: candy[k], rem)
            if valid_piles(p1, p2):
                found = True
                s1 = sum(p1)
                s2 = sum(p2)
                m = max(s1, s2)
                if m > res:
                    res = m
    print "Case #%d: %s" % (casenum, (res if found else "NO"))
            

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        cases = int(lines[0])
        for i in xrange(1, cases+1):
            candy = map(int, lines[i*2].split(' '))
            solve(candy, i) 
