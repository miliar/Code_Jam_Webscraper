#!/usr/bin/env python
# -*- coding: utf8 -*-

__author__    = "renaud blanch <rndblnch at gmail dot com>"
__copyright__ = "Copyright © 2010 - Renaud Blanch"
__licence__   = "GPLv3 [http://www.gnu.org/licenses/gpl.html]"

import sys
next_line = sys.stdin.next


"""
Candy Splitting
[http://code.google.com/codejam/contest/dashboard?c=975485#s=p2]
"""

def seans(Cis):
	s = 0
	for C in Cis:
		s ^= C
	if s != 0:
		return "NO"
	Cis.sort()
	return sum(Cis[1:])


T = int(next_line())
for X in xrange(T):
	print "Case #%s:" % (X+1),
	N = int(next_line().strip())
	Cis = [int(C) for C in next_line().strip().split()]
	assert len(Cis) == N
	print seans(Cis)
