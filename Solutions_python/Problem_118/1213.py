#!/usr/bin/python 

import sys
from math import ceil

f = open(sys.argv[1], 'r')

num_of_cases = int(f.readline())

case_counter = 1

palindrom_cache = {}

def isPalindrom(x):
	if palindrom_cache.has_key(x):
		return True if palindrom_cache[x] == 1 else False 
	else:
		if x == reverse(x):
			palindrom_cache[x] = 1
			return True
		else:
			palindrom_cache[x] = 0
			return False

def reverse(x):
	res = 0
	while (x != 0 ): 
		remainder = x % 10
		res = res * 10 + remainder
		x = int(x/10)

	return res

while case_counter <= num_of_cases:
	[ a, b ] = [ int(x) for x in f.readline().strip().split(' ') ]
	
	low = int(ceil(a**0.5))
	high = int(b**0.5) + 1 

	result = 0
	for i in xrange(low, high):
		if isPalindrom(i) and isPalindrom(i**2):
			result += 1

	print "Case #%i: %s" % ( case_counter, result)
	
	case_counter += 1
