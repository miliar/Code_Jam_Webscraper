#! /usr/bin/env python3
T = int(input())
for i in range(T):
	N = int(input())
	A = tuple(map(int, input().split()))
	print('Case #%d: %d.000000' % (i+1, sum(1 for a in A if a!=A[a-1])))