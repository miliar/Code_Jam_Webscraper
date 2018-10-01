#!/usr/bin/python
'''
Code Jam Round 1A 2013
Problem A. Bullseye
http://code.google.com/codejam/contest/2418487/dashboard
t = amount of paint
r = initial radius of first circle
amount of paint used for 1 circle radius r = 2 * r + 1
'''
import sys
from math import sqrt
#from pprint import pprint
debug = '-d' in sys.argv
#fh = sys.stdin
fh = open(sys.argv[1])

def countrings(r, t):
	used = 0
	i = 0
	while used <= t:
		used += 2 * (r+2*i) + 1
		i += 1
	return i - 1

cases = int(fh.readline()) # T
for case in range(1, cases+1):
	print 'Case #%i:' % case,
	r, t = [ int(i) for i in fh.readline().split() ]
	if debug:
		print 'r=%s t=%s' % (r, t),
	print countrings(r, t)
	#print 'solution, how many rings can be drawn'
	sys.stdout.flush()
