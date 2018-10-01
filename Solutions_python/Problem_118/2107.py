#!/usr/bin/python3

import sys
import math

def isPalindrome(n):
	i, j = 0, len(n) -1
	while i <= j:
		if n[i] != n[j]:
			return False
		i += 1
		j -= 1
	return True

def isSquare(n):
	return n ** (1/2) == int(n ** (1/2))


t = int(sys.stdin.readline().strip())
for i in range(0, t):
	count = 0
	l = sys.stdin.readline().strip()
	l = l.split(' ')
	a = int(l[0])
	b = int(l[1])
	a = math.ceil(math.sqrt(a));
	b = math.floor(math.sqrt(b));
	for j in range(a, b+1):
		if isPalindrome(str(j)) and isPalindrome(str(j * j)):
			count += 1
	print("Case #{}: {}".format(i+1, count))
