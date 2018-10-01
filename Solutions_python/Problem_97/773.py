#! /usr/bin/env python
from multiprocessing import Pool


def rotate(n, amt, total):
	exp = 10**amt
	shift = 10**(total-amt)
	front = n / exp
	rem = n % exp
	return (rem * shift) + front


def numpairs(n, B, seen):
	if seen[n]:
		return 0
	strn = str(n)
	pairs = 0
	x = 0
	total = len(strn)
	for i in range(1, total):
		m = rotate(n, i, total)
		if m > n and m <= B and not seen[m]:
			seen[m] = True
			x += 1
			pairs += x
	return pairs


def solve(el):
	A, B = el
	pairs = 0
	seen = [False] * 2000000
	for n in range(A, B):
		pairs += numpairs(n, B, seen)
	return pairs


def main(args):
	with open(args[1]) as infile:
		cases = int(infile.readline())
		to_solve = []
		for i in range(cases):
			A, B = [int(x) for x in infile.readline().strip().split()]
			to_solve.append((A, B))
		p = Pool(2)
		for i, pairs in enumerate(p.map(solve, to_solve)):
			print "Case #%d: %d" % (i+1, pairs)


if __name__ == '__main__':
	import sys
	main(sys.argv)