#!/usr/bin/env python

import sys, os, re, operator


def solve(f):
	f.readline()
	l = map(int, f.readline().split())
	xor = reduce(operator.xor, l, 0)
	if xor != 0: return 'NO'
	return sum(l) - min(l)


def main():
	tt = int(sys.stdin.readline())
	for t in xrange(tt):
		res = solve(sys.stdin)
		print "Case #%d:" % (t+1), res


if __name__ == "__main__":
	main()
