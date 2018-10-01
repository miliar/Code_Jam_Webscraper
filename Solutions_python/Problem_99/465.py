#!/usr/bin/env python

import sys


def keeptyping (p, numtyped, numtot):
	# expected:
	# (1 - p (ok)) * (numtot + numtot - numtyped + 2) ...
	# ... + p (ok) * (numtot - numtyped + 1)

	p_ok = reduce (lambda x, y: x * y, p)
	return (1 - p_ok) * (numtot + numtot - numtyped + 2) + p_ok * (numtot - numtyped + 1)



def giveup (p, numtyped, numtot):
	return 2 + numtot



def p_ok_till (p, till):
	# all ok
	if till == 0:
		return reduce (lambda x, y: x * y, p)

	if till == len (p):
		return 1 - p[0]

	p_ok = p[:-till]
	p_nok = 1 - p[-till]

	return reduce (lambda x, y: x * y, p_ok) * p_nok


def charsbs (tot, typed, numbs):
	return 2*numbs + tot - typed + 1


def backspace (p, numtyped, numtot):
	e_min = 10^99
	bs_min = 0

	for num_bs in range (1, numtyped+1):
		e = 0

		for ok_till in range (0, numtyped+1):
			p_case = p_ok_till (p, ok_till) 
			#print "ok_till ", ok_till, ", p: ", p_case

			if num_bs >= ok_till:
				# pw ok
				e += p_case * charsbs (numtot, numtyped, num_bs)
			else:
				# pw nok
				e += p_case * (charsbs (numtot, numtyped, num_bs) + numtot + 1)

		#print "expectation: ", e, ", for ", num_bs, "backspaces"
		if e < e_min:
			e_min = e
			bs_min = num_bs
		
	#print "min expectation: ", e_min, ", for ", bs_min, "backspaces"
	return e_min


def solve (casenum, p, numtyped, numtot):
	keep = keeptyping (p, numtyped, numtot)
	give = giveup (p, numtyped, numtot)
	bs = backspace (p, numtyped, numtot)

	#print "keep: ", keep, "give up: ", give, ", bs: ", bs, ", min: ", min (keep, give, bs)
	print "Case #%d: %f" % (casenum, min (keep, give, bs))



num_testcases = int (sys.stdin.readline())

for case in range (1, num_testcases+1):
	(numtyped, numtot) = map (int, sys.stdin.readline().split())
	p = map (float, sys.stdin.readline().split())

	solve (case, p, numtyped, numtot)

