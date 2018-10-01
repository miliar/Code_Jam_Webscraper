#!/usr/bin/env python3
import sys
import math
from fractions import Fraction
argc = len(sys.argv)
filename = sys.argv[1]
if argc > 2:
	casenumbers = list(map(int, sys.argv[2:]))
file = open(filename)
T = int(file.readline().rstrip())
for case in range(1,T+1):
	vidaelf = Fraction(file.readline().rstrip())
	if argc > 2 and not(case in casenumbers):
		continue
	generation = 1
	ancestorelf = vidaelf * 2
	possible = False
	while generation <= 40:
		if ancestorelf >= 1:
			elflog = math.log(ancestorelf.denominator, 2)
			if elflog == int(elflog):
				possible = True
				break
		generation+=1
		ancestorelf*=2	
	print ("Case #", case, ": ", sep="", end="")
	if possible:
		print(generation)
	else:
		print("impossible")
