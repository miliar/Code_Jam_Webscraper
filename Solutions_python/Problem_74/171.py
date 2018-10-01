#!/usr/bin/env python

import sys

def solve():
	l = sys.stdin.readline().split()
	a, l = l[0], l[1:]
	a = int(a)

	gO = 1
	gB = 1
	bO = 0
	bB = 0

	curr = 0
	
	for _ in range(a):
		t = l[0]
		i = int(l[1])
		l = l[2:]
		
		if t == 'O':
			T = 1 + max(abs(i-gO)-bO, 0)
			gO = i
			bB += T
			bO = 0
			curr += T
		else:
			T = 1 + max(abs(i-gB)-bB, 0)
			gB = i
			bO += T
			bB = 0
			curr += T

	return curr

n, = map(int, sys.stdin.readline().split())

for i in range(n):
	print "Case #{}: {}".format(i+1, solve())
