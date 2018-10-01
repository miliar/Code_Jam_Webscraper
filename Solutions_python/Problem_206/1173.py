#!/usr/bin/python3

import sys 

t = int(input())

for testcase in range(t): 
	(d, n) = map(int, input().split())
	latest = 0
	for horse in range(n):
		(k, s) = map(int, input().split())
		latest = max(latest, (d-k)/(s*1.0))

	print("Case #{0}: {1:.6f}".format(testcase+1, d/latest))
	