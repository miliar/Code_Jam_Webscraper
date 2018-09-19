#!/bin/env python
### Code Jam ###################################################################
# Qualifier Round
#   Problem A Solution
#
# Author: Brian Crockford (dosperm@gmail.com)
# Language used: Python 2.6.2
# Environment used:
#   Ubuntu 9.10 (64-bit)
#   GNU bash, version 4.0.33(1)-release (x86_64-pc-linux-gnu)
################################################################################
import sys

def printcase(n,b):
	print "Case #{0}: {1}".format(n,
			{True:"ON",False:"OFF"}[b])

T = int(sys.stdin.readline().rstrip())
for i in range(T):
	line = sys.stdin.readline().rstrip()
	N, K = map(int, line.split(' ', 1))
	printcase(i+1,
			K % (2**N) == (2**N)-1)
