#!/usr/bin/env python
import sys
import math

def readCJIn(filename):
	"""Reads the file.
	
	This function reads Google Code Jam input files and returns the number of inputs and a list containing the inputs"""
	file = open(filename)
	inputs = []
	for line in file:
		inputs.append(line.strip())
	file.close()
	return int(inputs[0]),inputs[1:len(inputs)]

def feq(a,b):
	"""Returns true if the difference between a and b are less than 1e-6"""
	if math.fabs(a-b)<0.000001:
		return True
	return False

inmag, inputs = readCJIn(sys.argv[1])

for i in range(0,inmag):
	ccase = i+1
	switches = 0
	s = int(inputs[0])
	inputs = inputs[1:]
	ss = inputs[:s]
	inputs = inputs[s:]
	q = int(inputs[0])
	inputs = inputs[1:]
	qs = inputs[:q]

	ssd = dict([(val, True) for val in ss])
	distinct = 0
	for query in qs:
		if ssd[query]:
			ssd[query] = False
			distinct+=1
		if distinct==s:
			switches+=1
			distinct=1
			ssd = dict([(val, True) for val in ss])
			ssd[query]=False
	print "Case #%d: %d"%(ccase,switches)

	inputs = inputs[q:]
