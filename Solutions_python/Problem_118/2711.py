#!/usr/bin/python

import sys
import math

def main():
	T = int(sys.stdin.readline())
	for test in xrange(T):
		A,B = sys.stdin.readline().split()
		A,B = int(A),int(B)
		count = 0
		for x in xrange(A,B+1):
			if isPalindrome(x) and perfectSquare(x):
				if isPalindrome(int(math.sqrt(x))):
					count +=1
	
		print "Case #%d: %d" %(test+1,count)

def isPalindrome(n):
	n = str(n)
	if len(n) < 2: return True
	if n[0] != n[-1]: return False
	else:
		return isPalindrome(n[1:-1])
def perfectSquare(n):
	a = int(math.sqrt(n))
	if a*a == n:
		return True
	else:
		return False
	
if __name__ == '__main__':
	main()