#!/usr/bin/env python

def solve(x, r, c):
    if x > r and x > c:
        return "RICHARD"
    if r * c % x:
        return "RICHARD"    
    if x == 1:
        return "GABRIEL"
    if x == 2:
        return "GABRIEL"
    if x == 3:
        if r == 1 or c == 1:
            return "RICHARD"
        return "GABRIEL"
    if x == 4:
        if r <= 2 or c <= 2:
            return "RICHARD"
        return "GABRIEL"

for case in xrange(int(raw_input())):
    print "Case #%d:" % (case+1),
    x, r, c = map(int, (raw_input().split()))
    print solve(x, r, c)
