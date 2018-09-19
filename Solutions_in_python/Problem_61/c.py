#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

com = {}
dp = {}

def combin(k, n):
	pr = (k, n)
	if pr in com:
		return com[pr]
	if k == 0:
		com[pr] = 1
		return com[pr]
	if k == n:
		com[pr] = 1
		return com[pr]
	if n == 0:
		com[pr] = 0
		return com[pr]
	
	com[pr] = combin(k, n-1)+combin(k-1, n-1)
	return com[pr]
		

def solve(n, l):
	pr = (n, l)
	if pr in dp:
		return dp[pr]
	if l == 1:
		dp[pr] = 1
		return dp[pr]
	if l == 2:
		dp[pr] = 1
		return dp[pr]
	if n == l + 1:
		dp[pr] = 1
		return dp[pr]

	ret = 0
	for i in range(1, l):
		ret = ret + solve(l, i)*combin(l-i-1,n-l-1)
	
	dp[pr] = ret
	return ret

T = int(sys.stdin.readline())

for cc in range(1, T+1):
	n = int(sys.stdin.readline())
	num = 0
	for i in range(1, n):
		num = num + solve(n, i)

	print "Case #%d: %d"%(cc, num%100003)
