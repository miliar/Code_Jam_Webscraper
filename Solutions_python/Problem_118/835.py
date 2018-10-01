#!/usr/bin/env python
import sys

def isPal(x):
	s = str(x)
	l = len(s)
	for i in range(0, l):
		if s[i] != s[l - 1 - i]:
			return False
	return True

def palify(x, dig):
	s = str(x)
	if x == 0:
		s = ""
	l = list(s)
	r = list(s)
	r.reverse()
	if dig >= 0:
		l.append(str(dig))
	l.extend(r)
	return int("".join(l))

poss = []
for x in range(0, 1000):
	for dig in range(-1, 9):
		if x > 0 or (x == 0 and dig > 0):
			y = palify(x, dig)
			if isPal(y*y):
				poss.append(y*y)

# print poss

fin = file(sys.argv[1])
T = int(fin.readline())
for nc in xrange(1, T+1):
	arr = fin.readline().strip().split()
	A = int(arr[0])
	B = int(arr[1])
	ans = 0
	for x in poss:
		if x >= A and x <= B:
			ans += 1
	print "Case #%d: %d" % (nc, ans)
fin.close()	
	
	
