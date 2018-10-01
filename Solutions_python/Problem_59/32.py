#!/usr/bin/python
# Author: Ivan Kazmenko
import sys
tests = int (sys.stdin.readline ())
for test in range (tests):
	n, m = [int (x) for x in sys.stdin.readline ().split ()]
	a = []
	for i in range (n):
		s = sys.stdin.readline ()[:-1].split ('/')[1:]
		a += [s]
	b = []
	for j in range (m):
		s = sys.stdin.readline ()[:-1].split ('/')[1:]
		b += [s]
	res = 0
	for j in range (m):
		for k in range (len (b[j])):
			s = b[j][:k + 1]
			if not s in a:
				a += [s]
				res += 1
	sys.stdout.write ('Case #%d: %d\n' % (test + 1, res))
