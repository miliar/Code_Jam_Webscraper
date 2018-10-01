# Using the 3rd party library "gmpy2"
# gmpy2 is covered under the GNU LGPL license and
# can be downloaded from http://code.google.com/p/gmpy/
import gmpy2
from gmpy2 import mpz
from gmpy2 import mpfr

import math
import sys


# Read data file into a list
lines = []
with open(sys.argv[1], "r", encoding="utf-8") as data_file:
	for line in data_file:
		lines.append(line.rstrip('\n'))
		
		
# Get total number of test cases
test_cases = int(lines[0])
del lines[0]


# Process each test case
case = 0
for line in lines:
	case += 1
	data = line.split(" ")
	currentRadius = mpz(data[0])
	paint = mpz(data[1])
	
	# Calculate next line area
	rings = 0
	flag = True
	blah = 0
	while flag:
		blah += 1
		innerArea = currentRadius * currentRadius
		outerArea = (currentRadius + 1) * (currentRadius + 1)
		lineArea = outerArea - innerArea
		# print("inner: " + str(innerArea))
		# print("outer: " + str(outerArea))
		# print("line: " + str(lineArea))
		# print("paint: " + str(paint))
		
		if lineArea <= paint:
			rings += 1
			paint -= lineArea
			currentRadius += 2
		else:
			flag = False
			
		#if blah > 20:
		#	break
		
	
	print("Case #" + str(case) + ": " + str(rings))