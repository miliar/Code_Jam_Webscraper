#!/usr/bin/env python3

# I'm participating in CodeJam to learn some Python (and because the problems are really interesting)
#
# The script expects it's input on stdin, and writes it's output to stdout
#
# This problem is really easy. If K+1 is divisible with 2**N, the light is on, otherwise it's off

import sys

def solvecase(t):
	print("Case #" + str(t) + ": ", end="")
	line = sys.stdin.readline().split()
	N = int(line[0])
	K = int(line[1])
	remainder = (K+1) % (2**N)
	if remainder == 0:
		bulbstate="ON"
	else:
		bulbstate="OFF"
	print(bulbstate)

# Number of test cases:
T = int(sys.stdin.readline())

# Solve all cases one by one:
for t in range(1, T+1):
	solvecase(t)
