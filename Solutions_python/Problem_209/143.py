#!/usr/bin/env python
import math
pi = math.pi

def find_best(Pan,already):
	max1 = -1
	testR = 0
	pos = 0
	i = 0
	for R,H in Pan:
		if (R > already):
			test = pi*R*R - pi*already*already + 2*pi*R*H
		else:
			test = 2*pi*R*H
		if (test > max1):
			max1 = test
			testR = R
			pos = i
		i += 1
	if (testR > already):
		already = testR
	del Pan[pos]
	return max1,already

def solve():
	N , K = [int(i) for i in raw_input().split()]
	Pan = [[int(i) for i in raw_input().split()] for _ in xrange(N)]
	already = 0 
	best = 0
	for i in xrange(K):
		best1,already = find_best(Pan,already)
		best += best1
	return best

def main():
    T = int(raw_input())
    for t in xrange(T):
    	sol = solve()
    	print "Case #{}: {}".format(t+1,sol)

if __name__ == '__main__':
	main()