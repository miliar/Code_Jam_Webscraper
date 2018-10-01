# coding: utf8

import os, sys, re, string


def solve(N, L, H, others):
	v = range(L, H + 1)
	for n in others:
		if n == 1:
			continue
		v = filter(lambda x: (x % n == 0) if x > n else n % x == 0, v)
	return 'NO' if len(v) == 0 else min(v)

def main():
	T = int(sys.stdin.readline())
	for i in xrange(1, T + 1):
		N, L, H = map(int, sys.stdin.readline().split(" "))
		others = map(int, sys.stdin.readline().split(" "))
		print "Case #%d: %s" % (i, solve(N, L, H, others))

if __name__ == '__main__':
	main()


