#!/usr/bin/python

import sys

C = int(sys.stdin.readline())

for i in range(1,C+1):
	x, r, c = map(int, sys.stdin.readline().split())
        if (r*c)%x > 0 or max(r,c) < x or min(r,c) < (x+1)/2 or x >= 7:
            a = "RICHARD"
        elif x <= 3:
            a = "GABRIEL"
        elif x == 4 and min(r,c) == 2:
            a = "RICHARD"
        elif x == 5 and min(r,c) == 3 and max(r,c) == 5:
            a = "RICHARD"
        elif x == 6 and min(r,c) == 3:
            a = "RICHARD"
        else:
            a = "GABRIEL"
	print 'Case #%d: %s' % (i, a)

