#!/usr/bin/env python3

from collections import deque

def parse():
	n, k = map(int, input().split())
	return n, k

def solve(n, k):
	q = deque([[n, 1]])
	while True:
		l = q[0][0]-1
		x, y = l//2+l%2, l//2
		k -= q[0][1]
		if k <= 0: return x, y
		if q[-1][0] == x: q[-1][1] += q[0][1]
		else: q.append([x, q[0][1]])
		if q[-1][0] == y: q[-1][1] += q[0][1]
		else: q.append([y, q[0][1]])
		q.popleft()

def main():
	for i in range(int(input())):
		n, k = parse()
		x, y = solve(n, k)
		print('Case #{}: {} {}'.format(i+1, x, y))

if __name__ == '__main__': main()