#!/usr/bin/env python

import sys

FILE = sys.stdin

basegain = 2
# def timeWithNFarms(fcnt, gain, C, F, X, suma=0.0):
# 	if fcnt == 0:
# 		return suma + X / gain
# 	else:
# 		return timeWithNFarms(fcnt - 1, gain + F, C, F, X, suma + (C / gain))
def timeWithNFarms(fcnt, F, X, suma=0.0):
	return suma + X / (basegain + fcnt * F)
	
def timeToGetNextFarm(C, gain):
	return C / gain

def solveCase():
	C, F, X = ([float(x) for x in (FILE.readline()).strip().split(' ')])[:3]
	timeToGetFarms = 0
	t1 = timeWithNFarms(0, F, X, timeToGetFarms)
	gain = basegain
	timeToGetFarms += timeToGetNextFarm(C, gain)
	gain += F
	t2 = timeWithNFarms(1, F, X, timeToGetFarms)
	fcnt = 2
	while t2 < t1:
		t1 = t2
		timeToGetFarms += timeToGetNextFarm(C, gain)
		gain += F
		t2 = timeWithNFarms(fcnt, F, X, timeToGetFarms) 
		fcnt += 1
	return t1

if len(sys.argv) > 1:
	FILE = open(sys.argv[1])

cases = int(FILE.readline())

for case in range(cases):
	print("Case #"+str(case+1)+": "+str(solveCase()))

