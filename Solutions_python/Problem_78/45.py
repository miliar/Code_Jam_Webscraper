#! /usr/bin/python

import sys
from fractions import *

f = open(sys.argv[1], 'rt')

for t in range(1, int(f.readline())+1):
	n, pd, pg = map(int, f.readline().split(' '))	
	
	nd = 100 / gcd(pd, 100)
	
	thing = (nd <= n) and (pd == 100 or pg != 100) and (pd == 0 or pg != 0)
	
	ans = 'Possible' if thing else 'Broken'
	
	print "Case #%d: %s" % (t, ans)
