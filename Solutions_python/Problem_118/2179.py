#!/usr/bin/python
import sys;
import string;
import math;

if len(sys.argv) != 2:
	print 'Usage: fair-and-square.py <input file>'
	exit()

try:
	f = open(sys.argv[1], 'r')
except:
	print "Could not open the file: " + sys.argv[1]
	exit()

def is_int(num):
	if (num == math.floor(num)):
		return True;

def is_palindrome(num):
	num = str(num)
	return num == str(int(num[::-1]))

def is_square(num):
	sqrt = math.sqrt(num)
	if is_int(sqrt):
		if is_palindrome(int(sqrt)):
			return True
	return False

def is_fair_and_square(num):
	if is_palindrome(num):
		if is_square(num):
			return True
	return False

def num_fair_and_square(low, high):
	count = 0
	i = low
	while i <= high:
		if is_fair_and_square(i):
			count += 1
		i += 1
	return count


sets = int(f.readline())

for i in range( 0, sets ):
	
	nums = map(int,string.split(f.readline(), ' '))
	
	print 'Case #' + str(i+1) + ':',
	print num_fair_and_square(nums[0], nums[1])
