import re

inFile = open("B-small-attempt0.in", 'r')
outFile = open("B-small-output.txt", 'w')
#inFile = open("test.txt", 'r')
#outFile = open("outTest.txt", 'w')

numCases = inFile.readline()
caseNumber = 0
for case in inFile.readlines():
	caseNumber += 1
	magic = re.split("(\W+)", case)

	idx = 0
	if int(magic[idx]) == 1:
		combination = magic[idx + 2]
		idx += 4
	else:
		idx += 2
		combination = None
	if int(magic[idx]) == 1:
		opposition = magic[idx + 2]
	else:
		opposition = None
	invocation = magic[-3]
	print combination, opposition, invocation
	
	invocationStack =  []
	idx = -1
	for i in invocation:
		invocationStack.append(i)
		trans = False
		idx += 1
		if (idx >= 1):
			if combination != None:
				if ((invocationStack[idx-1] + invocationStack[idx]) == combination[0:2]) or ((invocationStack[idx] + invocationStack[idx-1]) == combination[0:2]):
					invocationStack.pop()
					invocationStack.pop()
					invocationStack.append(combination[2])
					idx -= 1
					trans = True
		if (idx >= 1):
			if opposition != None:
				for j in invocationStack:
					if j == opposition[0] and i == opposition[1] and not trans:
						invocationStack = []
						idx = -1
					elif j == opposition[1] and i == opposition[0] and not trans:
						invocationStack = []
						idx = -1
		
	print invocationStack
	outString = "Case #" + str(caseNumber) + ": ["
	for element in range(len(invocationStack)):
		outString += invocationStack[element]
		if element < len(invocationStack) - 1:
			outString += ", "
	outString += "]\n"
	print outString
	outFile.write(outString)
	
inFile.close()
outFile.close()
