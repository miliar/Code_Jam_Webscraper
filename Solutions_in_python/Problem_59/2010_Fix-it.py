#!/usr/bin/python
from sys import stdin
import string
from sets import Set

def p(s):
	x = []
	x.append(s)
	while True:
		t = string.rsplit(s,'/',1)
		if(t[0] == ''):
			break
		x.append(t[0])
		s = t[0]
	return x

cases = int(stdin.readline())

for i in range(cases):
	a = Set()

	t = stdin.readline().rstrip().split()
	n = int(t[0])
	m = int(t[1])
	for j in range(n):
		d = stdin.readline().rstrip()
		for xx in p(d):
			a.add(xx)
	#print a
	x = len(a)
	for j in range(m):
		d = stdin.readline().rstrip()
		for xx in p(d):
			a.add(xx)
	#print a
	y = len(a)

	print 'Case #%d: %d' % ( ( i+1), (y-x) )
