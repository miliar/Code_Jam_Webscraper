#! /usr/bin/env python

from sys import stdin

ntest = input()

for test in range(ntest):
    line = [int(i) for i in stdin.readline().strip().split()]
    s, p = line[1:3]
    t = line[3:]
    t.sort(reverse=True)
    m = len([i for i in t if i>=3*p-2]) + min(s, len([i for i in t if 3*p-2>i>=3*p-4 and p>1]))
    print "Case #%d: %d" % (test+1, m)