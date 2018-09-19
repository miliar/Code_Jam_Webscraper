#!/usr/bin/python

# Constants definition
MINFLOAT = 1e-6

def isEqual(float_a, float_b):
	if abs(float(float_a) - float(float_b)) < MINFLOAT: return True
	else: return False



for case in xrange(input()):
	company = []
	changes = 0
	for i in xrange(input()):
		company.append(raw_input())
	
	available = company[:]

	for j in xrange(input()):
		s = raw_input()
		if s in available:
			available.remove(s)
			if len(available) == 0:
				available = company[:]
				available.remove(s)
				changes += 1

	print "Case #%d: %d" % (case + 1, changes)
