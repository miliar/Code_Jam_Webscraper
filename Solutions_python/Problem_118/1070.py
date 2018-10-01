#!/usr/bin/python

import sys

def esPalindromo(num):
	return str(num) == str(num)[::-1]

def espejar(s, medio=None):
	if (medio):
		return s+str(medio)+s[::-1]
	else:
		return s+s[::-1]

def fairAndSquaresUpToDigits(n):
	n = n / 2
	yield 1
	yield 4
	yield 9
	if (n%2==0):
		k = n/2
	else:
		k = (n-1)/2

	N = 10**k
	num = 1
	while num < N:
		s = str(num)
		if (len(s) %2 == 0):
			s2 = espejar(s)
			if (esPalindromo(int(s2)**2)):
				yield int(s2)**2
		else:
			for i in xrange(0,9):
				s2 = espejar(s,i)
				if (esPalindromo(int(s2)**2)):
					yield int(s2)**2
		num = num + 1


FandSQ = list(fairAndSquaresUpToDigits(5))

#~ print FandSQ

def myxrange(a1, a2=None, step=1):
    if a2 is None:
        start, last = 0, a1
    else:
        start, last = a1, a2
    while cmp(start, last) == cmp(0, step):
        yield start
        start += step
#~ #~
T =  int(raw_input())
for case in xrange(T):
	A, B = map(int,raw_input().split())
	cantidad = len([x for x in FandSQ if x >= A and x <= B])
	print "Case #"+str(case+1)+": "+str(cantidad)


