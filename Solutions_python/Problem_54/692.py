#!/usr/bin/python
# File: FairWarning.py
# Author: Nigel Struble (ASCII)
# Date: 5/08/2010
# purpose: a program to solve the Fair Warning puzzle

def factor(n,m):
	while(m!=0):
		t = m
		m = n % m
		n = t
	return n

import sys;
if len(sys.argv) != 2:
	print "wrong number of inputs"
else:
	fin = open(sys.argv[1], 'r')
	C = int(fin.readline())
	for case_number in range(1, C+1):
		_list = fin.readline()[:-1].split(' ' )[1:]
		number_list = []
		difference = []
		for i in range(len(_list)):
			number_list.append(int(_list[i]))
		
		for i in range(1,len(number_list)):
			difference.append(abs(number_list[i]-number_list[i-1]))
		if len(difference) > 1:
			smallest_factor = factor(difference[0],difference[1])
		else:
			smallest_factor = difference[0]
		for i in range(2,len(difference)):
			_factor = factor(difference[i], difference[i-1])
			if smallest_factor > _factor:
				smallest_factor = _factor
		if number_list[0] % smallest_factor == 0:
			y = 0
		else:
			y = (number_list[0]/smallest_factor +1 )*smallest_factor - number_list[0]
		print "Case #" + str(case_number) + ":",
		print y
	
