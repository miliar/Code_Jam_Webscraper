#!/usr/bin/env python
import cj
from itertools import *

def read(reader):
	N = reader/int
	s = [reader/int for _ in xrange(N)]
	return N, s

def printout(a, b):
	return '\n' + ' '.join([str(i) for i in a]) + '\n' + ' '.join([str(i) for i in b])

def solve(N, S):
	sums = {}
	for mask in product([True, False], repeat = N):
		a = [x for i, x in enumerate(S) if mask[i]]
		s = sum(a)
		if s in sums:
			return printout(a, sums[s])
		else:
			sums[s] = a
	return 'Impossible'


cj.jam(read, solve)