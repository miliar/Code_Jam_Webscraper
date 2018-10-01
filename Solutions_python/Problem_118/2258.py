#!/usr/bin/python -O

import sys
import math

def is_palindrome(i):
	s = str(i)
	return s == s[::-1]

def count_fas_in_range(min, max):
	lsqrt = int(math.ceil(math.sqrt(min)))
	usqrt = int(math.ceil(math.sqrt(max)))

	palindromes = []

	for i in xrange(lsqrt, usqrt+1):
		if is_palindrome(i):
			palindromes.append(i)
	
	count = 0

	for p in palindromes:
		sqr = p*p
		if sqr <= max and is_palindrome(sqr):
			count += 1
	return count

input_data = sys.stdin.readlines()
T = int(input_data[0])

for t in xrange(1,T+1):
	line = input_data[t]
	min = int(line.split()[0])
	max = int(line.split()[1])
	count = count_fas_in_range(min, max)
	print 'Case #' + str(t) + ': ' + str(count)
