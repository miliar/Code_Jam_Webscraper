#!/usr/bin/env python

import sys

def main():
	with open(sys.argv[1]) as f:
		solve(f)

def solve(f):
	lines = f.readlines()
	C = int(lines[0])
	for i in range(1, C+1):
		t = map(int, lines[i].split())[1:]
		answer = solve_real(t)
		print "Case #%d: %s" % (i, answer)

def solve_real(t):
	t.sort()
	G = t[1] - t[0]
	for i in range(2, len(t)):
		G = gcd(G, t[i] - t[i-1])
	r = t[0] % G
	if r == 0:
		return 0
	return G - r

def gcd(a, b):
	while b != 0:
		t = b
		b = a % b
		a = t
	return a

if __name__ == '__main__':
	main()