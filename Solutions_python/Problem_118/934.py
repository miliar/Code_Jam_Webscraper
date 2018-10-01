#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from math import sqrt

def int2str(num):
	sbl = '012'

	num, rem = divmod(num, 3)

	ret = ''
	while num:
		ret = sbl[rem] + ret
		num, rem = divmod(num, 3)

	ret = sbl[rem] + ret

	return ret

def interesting_numbers():
	for x in range(0,1000):
		yield str(x)

	x = int("1000", base=3)

	while True:
		yield int2str(x)
		x = x+1


def gen_palindromes():
	gen = interesting_numbers()

	for as_s in gen:

		if as_s.startswith('0'):
			as_s = ''

		for c in list("0123456789") + ['']:
			if as_s:
				yield int(as_s + c + as_s[::-1])
			else:
				if c:
					yield int(c)
				else:
					continue

#def is_palindrome(x):
#	x = str(x)
	
#	for idx in range(len(str(x))/2+1):
#		if x[idx] != x[-(idx+1)]:
#			return False
#	return True

is_palindrome = lambda x: str(x) == ''.join(reversed(str(x)))

def palindrome_squares():
	generator = gen_palindromes()

	for palindrome in generator:
		if is_palindrome(palindrome*palindrome):
			yield palindrome*palindrome

def fair_square_between(a,b):
	n = 0

	gen = palindrome_squares()
	for p in gen:
		if a <= p <= b:
			n = n + 1
		elif p > 1000*b:
			break

	return n

def solve():
	a, b = map(int, sys.stdin.readline().strip().split(' '))

	return fair_square_between(a,b)

if __name__ == "__main__":
	N = int(sys.stdin.readline().strip())

	for n in range(N):
		num = solve()

		print "Case #{n}: {num}".format(n=n+1, num=num)
