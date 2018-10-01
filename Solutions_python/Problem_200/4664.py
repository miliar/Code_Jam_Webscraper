#!/usr/bin/python3

def tiny(x) :
	digit = x%10
	while (x != 0) :
		x = int(x/10)
		if digit >= x%10 :
			digit = x%10
		else :
			return False
	return True

def findTiny(x) :
	found = False
	while ( not found) :
		if tiny(x) :
			found = True
		else :
			x -= 1
	return x

testCase = int(input())
for case in range(1,testCase+1) :
	x = int(input())
	print ('Case #{}: {}'.format(case,findTiny(x)))