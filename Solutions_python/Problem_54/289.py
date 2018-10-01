#!/usr/bin/python

from random import randint

def gcd(a, b):
    if a == 0: return b
    while b:
        a,b = b,a%b
    return a

def getfactor(s):
    f = None
    for a in s:
        for b in s:
            if a <= b: continue
            if not f:
                f = (a-b)
            else:
                f = gcd(f, a-b)
            if f == 1: return 1
    return f

def solve(s):
	w = getfactor(s)
	s = [(w-(x%w))%w for x in s if (w-(x%w))%w]
	if not s:
		return 0
	return reduce(lambda x,y: x*y/gcd(x,y), s[1:], s[0])

def bfsolve(s):
	ans = 0
	best = 1
	for k in xrange(1000):
		x = [x+k for x in s]
		tmp = reduce(gcd, x[1:], x[0])
		if best < tmp:
			best = tmp
			ans = k
	return ans

for nCase in xrange(int(raw_input().strip())):
	s = map(int, raw_input().strip().split(" ")[1:]) 
	print "Case #%d: %d" % (nCase+1, solve(s))
