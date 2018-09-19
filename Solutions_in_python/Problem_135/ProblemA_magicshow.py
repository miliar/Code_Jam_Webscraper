#!/usr/bin/python

# Read Input
fname = "A-small-attempt0.in"
FileContent = []
with open(fname) as f:
	FileContent = f.readlines()
	
# First line = number of test cases
NumCases = int(FileContent[0])

i = 1

for t in range(1,NumCases+1):

	# Read answer to first question
	Answer1 = int(FileContent[i])
	i += 1
	# Read layout
	Row1 = FileContent[i + (Answer1-1)].split()
	i += 4
	# Read answer to second question
	Answer2 = int(FileContent[i])
	i += 1
	# Read layout
	Row2 = FileContent[i + (Answer2-1)].split()
	i += 4
	
	#print Row1
	#print Row2
	
	cntMatch = 0
	match = -1
	for r in Row1:
		if r in Row2:
			match = r
			cntMatch += 1
	
	# Case Answer String		
	if cntMatch == 0: 	# no matches
		CaseAnswer = "Volunteer cheated!"
	elif cntMatch == 1:	# one match
		CaseAnswer = match
	else:				# multiple matches
		CaseAnswer = "Bad magician!"
	
	# Output!
	output = "Case #%d: %s" % (t, CaseAnswer)
	print output