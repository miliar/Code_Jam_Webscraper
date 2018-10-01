#!/usr/bin/env python2
import sys

def flip(S, K, p):
	res = S[:]
	for a in xrange(p,p+K):
		res[a] = not res[a]

	return res

def solve(S, K):
	L = len(S)
	p = 0
	res = 0

	while p<(L-K+1):
		if not S[p]:
			res += 1
			S = flip(S,K,p)
		p += 1

	return '%d' % res if S.count(True) == len(S) else 'IMPOSSIBLE'

cases = int(sys.stdin.readline())

for case in range(cases):
	D = 0
	line = sys.stdin.readline()[:-1].split(' ')
	S = [ x == '+' for x in line[0]]
	K = int(line[1])
	print ("Case #%d: %s" % (case+1,solve(S, K)))
