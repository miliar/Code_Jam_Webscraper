#!/usr/bin/env pypy
# -*- coding: utf8 -*-

__author__    = "renaud blanch <rndblnch at gmail dot com>"
__copyright__ = "Copyright © 2011–2013 - Renaud Blanch"
__licence__   = "GPLv3 [http://www.gnu.org/licenses/gpl.html]"

from common import nt, ni, nl, line


"""
Lawnmower
"""

def max_line(lawn):
	return [
		list(u < max(line) for u in line)
		for line in lawn
	]

def possible(N, M, lawn):
	lines   = max_line(lawn)
	columns = zip(*max_line(zip(*lawn)))
	for i in xrange(N):
		for j in xrange(M):
			if lines[i][j] and columns[i][j]:
				return False
	return True

T = ni(); nl()
for X in xrange(T):
 	print "Case #%s:" % (X+1),
	N, M = ni(), ni()
	nl()
	lawn = [list(line(int)) for _ in xrange(N)]
	assert (len(lawn), len(lawn[0])) == (N, M)
	print "YES" if possible(N, M, lawn) else "NO"
