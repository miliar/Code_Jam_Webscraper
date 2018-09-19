#!/usr/bin/env python3

import sys
from math import sqrt,ceil,floor
from functools import lru_cache

def palindrome(x):
	s = str(x)
	m = len(s)//2
	return s[:m] == s[:-(m+1):-1]

@lru_cache(maxsize=None)
def fas(x):
	# returns true if x**2 is fas, not x !
	return palindrome(x) and palindrome(x**2)

with open(sys.argv[1]) as file:
	t = int(file.readline()[:-1])
	for i in range(1,t+1):
		a,b = file.readline().split()
		sa,sb = (ceil(sqrt(int(a))), floor(sqrt(int(b)))+1)
		print("Case #%d: %d" % (i, len([x for x in range(sa,sb) if fas(x)])))
