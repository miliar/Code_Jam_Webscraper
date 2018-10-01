from math import *

def is_palindrome(x):
	s = str(x)
	s2 = s[::-1]
	return s == s2

def is_square_of_palindrome(x):
	r = sqrt(x)
	if r == floor(r) and is_palindrome(int(r)):
		return True
	else:
		return False

def fair_and_square(x):
	return is_palindrome(x) and is_square_of_palindrome(x)

T = int(raw_input())
for t in range(T):
	line = raw_input().split()
	A = int(line[0])
	B = int(line[1])
	count = 0
	for i in range(A, B+1):
		if fair_and_square(i):
			count += 1
	print "Case #%d: %d"%(t+1, count)
	
