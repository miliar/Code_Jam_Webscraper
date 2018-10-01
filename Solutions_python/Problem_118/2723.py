#!/usr/bin/python

import sys

def palindromes(N):
	return [x for x in xrange(1, N) if is_palindrome(x)]

def squares(l):
	return map(lambda x: pow(x, 2), l)

def filter_palindromes(l):
	return filter(lambda x: is_palindrome(x), l)

def get_fair_and_square(N):
	return filter_palindromes(squares(palindromes(N)))

def is_palindrome(n):
	s = str(n)
	return s == s[::-1]

def get_sublist(A, B, l):
	return [x for x in xrange(A, B + 1) if x in l]

def main():
	# Small
	N = 100

	# Large 1
	# N = pow(10, 7)

	# Large 2
	# N = pow(10, 10)
	
	fair_and_square = get_fair_and_square(N)
	# print fair_and_square

	# T = int(input())
	T = int(sys.stdin.readline())
	# print T

	for t in xrange(T):
		# A = int(input())
		# B = int(input())
		A, B = [int(x) for x in sys.stdin.readline().split(' ')]
		# A = l[0]
		# B = l[1]
		print 'Case #' + str(t + 1) + ":" ,
		print len(get_sublist(A, B, fair_and_square))

if __name__ == '__main__':
	main()
	