#!/usr/bin/env pypy
# -*- coding: utf8 -*-

__author__    = "renaud blanch <rndblnch at gmail dot com>"
__copyright__ = "Copyright © 2011–2013 - Renaud Blanch"
__licence__   = "GPLv3 [http://www.gnu.org/licenses/gpl.html]"

from common import nt, ni, nl, line


"""
Fair and Square
"""

from math import sqrt, floor, ceil
from itertools import chain

def palindrome(l, c, r):
	if l == 0:
		return c
	l = str(l)
	if r:
		p = "".join(chain([l, str(c)], reversed(l)))
	else:
		p = "".join(chain([l], reversed(l)))
	return int(p)
	
def palindromes(a):
	n = len(str(a))
	n, r = n/2, n%2
	n = 10**n
	l, c = a/n, 0
	if r == 1:
		l, c = l/10, l%10-1
		if c < 0:
			l, c = l-1, c+1
	while True:
		yield palindrome(l, c, r)
		if r == 0:
			l += 1
			if l >= n:
				l, c, r = n/10, 0, 1
		else:
			c += 1
			if c > 9:
				c = 0
				l += 1
				if l >= n:
					l, c, r = n, 0, 0
					n *= 10
	

def is_palindrome(p):
	p = str(p)
	l = len(p)
	return all(p[i] == p[l-i-1] for i in range(l/2))

def fair_and_square(A, B):
	a = int(floor(sqrt(A)))
	assert a*a <= A
	Ps = []
	for p in palindromes(a):
		P = p*p
		if B < P:
			break
		if A <= P:
			if is_palindrome(P):
				Ps.append(P)
	return len(Ps)

T = ni(); nl()
for X in xrange(T):
 	print "Case #%s:" % (X+1),
	A, B = ni(), ni()
	nl()
	assert A <= B
	print fair_and_square(A, B)
