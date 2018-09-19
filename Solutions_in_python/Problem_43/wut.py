#!/usr/bin/env python

from copy import copy

def ans(N):
	N = list(N)
	base = max([len(set(N)), 2])
	S = [1, 0] + range(2, base)
	S.reverse()
	M = {}
	for i, n in enumerate(N):
		if not M.has_key(n):
			M[n] = S.pop()
		N[i] = M[n]
	N.reverse()
	for i, n in enumerate(N):
		N[i] *= base**i
	return sum(N)



with open('in.txt') as fin:
	with open('out.txt', 'w') as fout:
		T = int(fin.readline().strip())
		for case in xrange(T):
			N = fin.readline().strip()
			print >>fout, 'Case #%d: %d' % (case+1, ans(N))
