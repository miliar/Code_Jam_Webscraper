#!/usr/bin/python

import time
import math

def isPalindrome(number):
	string = str(number)
	reversed = string[::-1]
	return string == reversed
	
def isFairAndSquare(number):
	if isPalindrome(number):
		square = math.sqrt(number)
		if int(square) == float(square) and isPalindrome(int(square)):
#				print 'Fair and square:', number, square
			return True
	return False
	
fp = open('C-small-attempt0.in')
fpout = open('output.txt', 'w')
cases = int(fp.readline())

for c in range(cases):
	number = 0
	[A, B] = [int(x) for x in fp.readline().split()]

	for i in range(A, B + 1):
		if isFairAndSquare(i):
			number += 1

	output = 'Case #%d: %d\n' %(c + 1 , number)
	fpout.write(output)