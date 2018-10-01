# -*-coding:Utf-8 -*

import sys, pprint
pp = pprint.PrettyPrinter(indent=4)

# Parse args
with open("C-small-attempt1.in") as f:
	arg = f.readlines()

T = int(arg[0])
case = [[0 for y in range(2)] for x in range(int(T))]
for ct in range(T):
	case[ct][0] = int(arg[1+ct*2].split()[1])
	case[ct][1] = arg[2+ct*2].replace("\n", "")

# Precompile Quaternion rules for fast resolution
quaternion = dict()
quaternion['1'] = dict()
quaternion['1']['1'] = '1'
quaternion['1']['i'] = 'i'
quaternion['1']['j'] = 'j'
quaternion['1']['k'] = 'k'
quaternion['i'] = dict()
quaternion['i']['1'] = 'i'
quaternion['i']['i'] = '-1'
quaternion['i']['j'] = 'k'
quaternion['i']['k'] = '-j'
quaternion['j'] = dict()
quaternion['j']['1'] = 'j'
quaternion['j']['i'] = '-k'
quaternion['j']['j'] = '-1'
quaternion['j']['k'] = 'i'
quaternion['k'] = dict()
quaternion['k']['1'] = 'k'
quaternion['k']['i'] = 'j'
quaternion['k']['j'] = '-i'
quaternion['k']['k'] = '-1'

# Mirror-build the Quarternion table for negatives values
quartenionValues = ['1', 'i', 'j', 'k']
for v in quartenionValues:
	for n in quartenionValues:
		if quaternion[v][n][0] == '-':
			quaternion[v]['-' + n] = quaternion[v][n][1]
		else:
			quaternion[v]['-' + n] = '-' + quaternion[v][n]

for n in quartenionValues:
	quaternion['-' + n] = dict()
	for v in quartenionValues:
		if quaternion[n][v][0] == '-':
			quaternion['-' + n][v] = quaternion[n][v][1]
		else:
			quaternion['-' + n][v] = '-' + quaternion[n][v]

for n1 in quartenionValues:
	for n2 in quartenionValues:
		quaternion["-" + n1]["-" + n2] = quaternion[n1][n2]

# Neutral values, useful for initializing or after finding a letter
quaternion[''] = dict()
for v in quartenionValues:
	quaternion[''][v] = v
for n in quartenionValues:
	quaternion['']["-" + n] = "-" + n

# pp.pprint(quaternion)


	
f = open('C.out','w')

# Compute each case
for ct in range(int(T)):
	# Print data in memory
	# print "*************** case number " + str(ct)
	# print "list : " + case[ct][1] + " x " + str(case[ct][0])

	# BAD IDEA. My computer probably doesn't have enougth RAM for this to work
	# clist = ''
	# for x in range(case[ct][0]):
	# 	clist = clist + case[ct][1]
	# print "Total list : " + clist

	# Initialize the search
	currentIteration = 0
	# Use the unique-key property of dict to remove duplicate
	currentComputation = dict()
	currentComputation[('', 'i')] = True

	# Unraveal the string
	# (We DON'T add it in memory due to it's sheer size)
	while(currentIteration < case[ct][0]):
		currentLetter = 0
		while(currentLetter < len(case[ct][1])):
			letter = case[ct][1][currentLetter]
			# Make a copy to avoir infinite loop (just in case)
			invariantComputation = dict(currentComputation)
			# For each search...
			for (value, objective) in invariantComputation:
				# Remove the current calculation
				currentComputation.pop((value, objective), None)
				
				# Multiply !
				currentComputation[quaternion[value][letter], objective] = True

				# and if we find a new goal, add a new search
				if quaternion[value][letter] == objective:
					if objective == "i":
						currentComputation['', 'j'] = True
					if objective == "j":
						currentComputation['', 'k'] = True
			currentLetter += 1
		currentIteration += 1

	# Check if one of the string have find something
	found = "NO"
	for (value, objective) in currentComputation:
		if value == "k" and objective == "k":
			found = "YES"
			break
	
	print "Case #" + str(ct+1) + ": " + found
	
	# Write output
	f.write ("Case #" + str(ct+1) + ": " + found + "\n")

f.close()
