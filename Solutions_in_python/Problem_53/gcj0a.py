#!/usr/bin/env python3.1

def calc(n, k):
	for i in range(1,n+1):
		if k % 2 != 1: return "OFF"
		k = (k - 1) / 2
	return "ON"

import sys
lines = sys.stdin.read().split("\n")

numTestCases = int(lines[0])
lines = lines[1:]

for i in range(numTestCases):
	args = lines[i].split(" ")
	result = calc(int(args[0]), int(args[1]))
	print("Case #%d: %s" % (i+1, result))
