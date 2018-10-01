#!/usr/bin/env python

# Google code jam 2010 : pure

import sys

def binomial(n):
    b = [0] * (n+1)
    b[0] = 1
    for i in xrange(1, n+1):
	b[i] = 1
	j = i-1
	while j > 0:
	    b[j] += b[j-1]
	    j -= 1
    return b

# p < n
def res(p,n):
    if p == 1:
	return 1
    elif p == (n-1):
	return 1
    else:
	count = 0
	binom = binomial(n-p-1)
	for k in range(2*p-n,p):
	    if k > 0:
		count = count + binom[p-k-1] * res(k,p)
	return count

def result(n):
    sum = 0
    for p in range(1,n):
	#print p
	#print res(p,n)
	sum = sum + res(p,n)
    return sum%100003

p = int(sys.stdin.readline())
cases = []
for s in range(1,p+1):
    line = sys.stdin.readline()
    n = int(line)

    print "Case #" + str(s) + ": " +  str(result(n))

