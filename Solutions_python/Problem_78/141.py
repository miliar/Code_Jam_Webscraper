#!/usr/local/bin/python

# A. FreeCell Statistics

import math
import sys
from fractions import gcd

f = sys.stdin
T = int(f.readline())

for x in range(1, T+1):
	list = [int(e) for e in f.readline().split()]
	n = list[0] 
	pd = list[1]
	pg = list[2]

	stepD = 100 / gcd(100, pd)
	if stepD <= n:
		y = "Possible"
	else:
		y = "Broken"

	if pd < 100 and pg == 100: 
		y = "Broken"
	if pd > 0 and pg == 0: 
		y = "Broken"

	print "Case #%d: %s" % (x, y)
