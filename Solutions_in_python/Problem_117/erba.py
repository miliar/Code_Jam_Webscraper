#!/usr/bin/env python

import sys
import operator
from math import sqrt, floor, ceil

class InputFile:
	def __init__(self, fd):
		self.fd = fd
	def readInt(self):
		return int(self.fd.readline())
	def readIntegers(self):
		return tuple([int(x) for x in self.fd.readline().split()])
	def readIntegersList(self):
		return [int(x) for x in self.fd.readline().split()]
	def readString(self):
		return self.fd.readline()[:-1]

def solve(a, rig, col):
	if rig == 1 or col == 1:
		return True
	
	massimoRig = [0]*rig
	for r in range(rig):
		massimoRig[r] = -1
		for c in range(col):
			if a[r][c] > massimoRig[r]:
				massimoRig[r] = a[r][c]
	
	massimoCol = [0]*col
	for c in range(col):
		massimoCol[c] = -1
		for r in range(rig):
			if a[r][c] > massimoCol[c]:
				massimoCol[c] = a[r][c]
	
	for r in range(rig):
		for c in range(col):
			x = a[r][c]
			maxRig = massimoRig[r]
			maxCol = massimoCol[c]
			
			if x < maxRig:
				if not x == maxCol:
					return False
	
			if x < maxCol:
				if not x == maxRig:
					return False
	
	return True


inputfile = InputFile(sys.stdin)
T = inputfile.readInt()
for n in range(1,T+1):
	(rig, col) = inputfile.readIntegers()
	
	a = []
	for k in range(rig):
		a.append(inputfile.readIntegersList())
	
	result = solve(a, rig, col)
	if result:
		print "Case #%d: YES" % n
	else:
		print "Case #%d: NO" % n

