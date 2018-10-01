#!/usr/bin/python
from sys import argv
from gmpy import is_square
from math import sqrt

with open(argv[1], "r") as f:
	x = f.readline()
	lines = f.readlines()

T = 0

def is_palindrome(number):
	string_number = str(number)
	if len(string_number) == 1:
		return True
	else:
		list_number = list(string_number)
		original = list(list_number)
		list_number.reverse()
		return  original == list_number

for line in lines:
	T += 1
	start , end = line.strip().split()
	interval = xrange(eval(start), eval(end)+1)
	fair_and_square = [number
						for number in interval
							if is_palindrome(number) and is_square(number) and is_palindrome(int(sqrt(number)))
					]
	print "Case #{0}: {1}".format(T, len(fair_and_square))