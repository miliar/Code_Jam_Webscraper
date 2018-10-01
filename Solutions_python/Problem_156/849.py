#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
import sys

class InputFile:
	def __init__(self, fd):
		self.fd = fd
	def readInt(self):
		return int(self.fd.readline())
	def readIntegers(self):
		return tuple([int(x) for x in self.fd.readline().split()])
	def readFloats(self):
		return tuple([float(x) for x in self.fd.readline().split()])
	def readIntegersList(self):
		return [int(x) for x in self.fd.readline().split()]
	def readString(self):
		return self.fd.readline()[:-1]

def columnTimeToReach(c, h):
	return (c-1) // h

def listTimeToReach(p, h):
	return sum([columnTimeToReach(c, h) for c in p])

def solve(p):
	maximum = max(p)
	best = maximum
	for h in range(1, maximum+1):
		time = listTimeToReach(p, h)
		if time + h < best:
			best = time + h
	return best

inputfile = InputFile(sys.stdin)
T = inputfile.readInt()
for test in range(1,T+1):
	d = inputfile.readInt()
	p = inputfile.readIntegersList()
	assert(len(p) == d)

	result = solve(p)
	
	print "Case #{test}: {result}".format(test=test, result=result)
