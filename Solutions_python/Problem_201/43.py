# coding: utf-8
import sys
import itertools
import heapq

#filename = "C-small-2-attempt0.in"
#filename = "test2.in"
filename = None


def divide(n):
	if n % 2 == 1:
		return (n/2, n/2)
	else:
		return (n/2, n/2 -1)

def solve(n, k):
	h = {}
	h[n] =  1
	nbPersons = k
	while nbPersons > 1:
		maxInterval = max(h.keys())
		nbPlace= min(h[maxInterval], nbPersons-1)

		h[maxInterval] -= nbPlace
		if(h[maxInterval] == 0):
			h.pop(maxInterval, None)
		l, r = divide(maxInterval)
		nbPersons-= nbPlace
		if(l > 0):
			h[l] = h.setdefault(l,0) + nbPlace
		if(r > 0):
			h[r] = h.setdefault(r,0) + nbPlace
		

	maxInterval = max(h.keys())
	h[maxInterval] -= 1
	l, r = divide(maxInterval)
	return max(l,r), min(l,r)

def main():
	if filename:
		file = open(filename)
	else:
		file = sys.stdin


	T = int(file.readline().strip())
	for i in range(T):	
		N, k = map(int, file.readline().strip().split())
		
		l, r = solve(N, k)
		print "Case #%d: %d %d" % (i+1, l, r)
		

	if file is not sys.stdin:
	    file.close()


if __name__ == '__main__':
	main()
	
