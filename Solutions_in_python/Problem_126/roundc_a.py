input_file = open('A-small-attempt0.in')
countlines = 0
caseNum = 0
vowels = ["a","e","i","o","u"]

for line in input_file:
	if countlines == 0:
		numOfCases = int(line)
		countlines+=1
		continue
	caseNum+=1
	workingIndices = []
	dummyIndex = []
	word, length = line.split(" ")
	length = int(length)
	for i in xrange(length):
		if i == 0:
			for charIndex in xrange(len(word)):
				if word[charIndex] not in vowels:
					workingIndices.append(charIndex)
			# print "I1"
			# print workingIndices 
		else:
			dummyIndex = []
			for charIndex in workingIndices:
				# print charIndex
				if(charIndex < len(word)-1 and word[charIndex+1] not in vowels):
					dummyIndex.append(charIndex+1)
			workingIndices = dummyIndex
#			print i
#			print workingIndices
	dummyIndex = []
	for i in workingIndices:
		dummyIndex.append(i-length+1)
	workingIndices = dummyIndex
	answer = 0
	for i in xrange(len(workingIndices)):
		if i == 0:
			answer += (workingIndices[i]+1)*(len(word) - length - workingIndices[i] + 1)
		else:
			answer += (workingIndices[i]-workingIndices[i-1])*(len(word)-workingIndices[i] - length + 1)

	print "Case #" + str(caseNum) + ": " + str(answer)


