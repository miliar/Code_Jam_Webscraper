#!/usr/bin/env python2

import sys,math

def first(s):
    st = s[0]
    ate = 0
    for n in xrange(1, len(s)):
        if st > s[n]:
            ate += st - s[n]
        st = s[n]
    return ate

def second(s):
    st = s[0]
    maxrate = 0
    for n in xrange(1, len(s)):
        if st > s[n]:
            crate = st - s[n]
            if crate > maxrate:
                maxrate = crate
        st = s[n]
    ate = 0
    for st in s[:-1]:
        ate += min(st, maxrate)
    return ate

def readinput(f):
    test_cases = int(f.readline())
    for ncase in range(test_cases):
        times = int(f.readline())
        s = [int(c) for c in f.readline().split(' ')]
        yield first(s), second(s)

if __name__=="__main__":
    n = 1
    for case in readinput(sys.stdin):
        print "Case #%d: %d %d" % (n, case[0], case[1])
        n += 1
