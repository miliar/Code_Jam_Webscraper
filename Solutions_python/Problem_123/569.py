# Using the 3rd party library "gmpy2"
# gmpy2 is covered under the GNU LGPL license and
# can be downloaded from http://code.google.com/p/gmpy/
import gmpy2
from gmpy2 import mpz

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
for i in range(test_cases):

	case += 1
	operations = 0
	
	# Get input data
	my_mote = int(lines[0].split(" ")[0])
	num_other_motes = int(lines[0].split(" ")[1])
	del lines[0]
	
	other_motes = [int(x) for x in lines[0].split(" ")]
	other_motes.sort()
	del lines[0]
	
	
	# First, find if immediately solveable
	for j in range(num_other_motes):
		if my_mote > other_motes[j]:
			my_mote += other_motes[j]
		else:
			# How many motes until we're done?
			# eg, how many operations if we just remove the rest?
			remove_ops = num_other_motes - j
			
			# How many motes have to add to make it solvable?
			unsolved = True
			temp_operations = 0
			temp_my_mote = my_mote
			while unsolved:
				if temp_my_mote > other_motes[j]:
					temp_my_mote += other_motes[j]
					unsolved = False
				# If mote is too small to eat anything, just remove next
				elif temp_my_mote == 1:
					temp_operations += 1
					unsolved = False
				else:
					temp_my_mote += (temp_my_mote - 1)
					temp_operations += 1

					
			# Which is cheaper: adding or removing?
			if temp_operations < remove_ops:
				my_mote = temp_my_mote
				operations += temp_operations
			else:
				operations += remove_ops
				break
				
	
	print("Case #" + str(case) + ": " + str(operations))
		
		