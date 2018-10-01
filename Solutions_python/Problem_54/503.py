#!/usr/bin/env python

import sys
import fractions

def findGCD(l):
		
	if (len(l) > 0):
		gcd = l[0]
		for i in l:
			gcd = fractions.gcd(gcd, i)
		
		return gcd
		
	else:
		return 1

def calculateTime(l):
	
	int_list = [int(i) for i in l]
	int_list.sort()
	
	length = len(int_list)
	
	diff_list = []
	
	for i in range(length - 1):
		diff_list.append(int_list[i+1] - int_list[i])
		
	diff_list.sort()
	
	gcd = findGCD(diff_list)
	
	modulus = int_list[0] % gcd
	
	if (modulus > 0):
		return (gcd - modulus)
	else:
		return 0
		

if __name__ == '__main__':

	inp_file = sys.argv[1]
	op_file = sys.argv[2]
	
	inp = open(inp_file, 'r')
	op = open(op_file, 'w')
	
	C = int(inp.readline())
	
	for i in range(1, C+1):
		values = inp.readline().split()
		ans = calculateTime(values[1:])
		
		op.write('Case #%d: %d\n' % (i, ans))
	
	inp.close()
	op.close()
	