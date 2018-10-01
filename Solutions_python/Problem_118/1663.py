#!/usr/bin/python

import sys

l = []
for i in xrange(1, 10 ** 7):
    if not i == int(str(i)[::-1]):
        continue
    x = i * i
    if x == int(str(x)[::-1]):
        l.append(x)

T = int(sys.stdin.readline())

def solve():
    a,b = map(int, sys.stdin.readline()[:-1].split())
    x = None
    for i in xrange(len(l)):
        if x is None and l[i] >= a:
            x = i
        if l[i] > b:
            return i - x
    if x is None:
        return 0
    else:
        return i - x + 1

for i in xrange(T):
    x = solve()
    print 'Case #%d: %d' % (i+1, x)
