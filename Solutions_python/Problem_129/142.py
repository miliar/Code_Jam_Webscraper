from __future__ import print_function
import sys
from collections import defaultdict
import heapq

T = int(sys.stdin.readline())

def c(o, e):
	x = e - o
	return (x * x + 3 * x) / 2


def solve(N, oep):
	geton = defaultdict(int)
	getoff = defaultdict(int)
	intcost = 0
	for o, e, p in oep:
		geton[o] += p
		getoff[e] += p
		intcost += p * c(o, e)
	cost = 0
	ticket_orig = []
	ticket_amt = []
	for i in range(1, N+1):
		if i in geton:
			ticket_orig.append(i)
			ticket_amt.append(geton[i])
		while getoff[i] != 0:
			if getoff[i] < ticket_amt[-1]:
				orig = ticket_orig[-1]
				cost += getoff[i] * c(orig, i)
				#print(getoff[i], orig, i)
				ticket_amt.append(ticket_amt.pop() - getoff[i])
				getoff[i] = 0
			else:
				num = ticket_amt.pop()
				orig = ticket_orig.pop()
				cost += num * c(orig, i)
				#print(num, orig, i)
				getoff[i] -= num
	return cost - intcost




for i in range(T):
	N, M = [int(x) for x in sys.stdin.readline().split()]
	oep = [[int(x) for x in sys.stdin.readline().split()] for j in range(M)]
	print("Case #" + str(i+1) + ": " + str(solve(N, oep)))