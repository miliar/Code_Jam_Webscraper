#! /usr/bin/python

import sys
from itertools import *

def pAdd(l):
	return reduce(lambda x,y: x^y, l)

f = open(sys.argv[1], 'rt')

for t in range(1, int(f.readline())+1):

	n = int(f.readline())
	l = map(int, f.readline().split(' '))

	if reduce(lambda x,y: x^y, l) == 0:
		s = str( sum(l) - min(l) )
	else:
		s = 'NO'
	print "Case #%d: %s" % (t, s)
