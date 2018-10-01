from sets import Set
file1 = open("q1Test.txt","r")
numOfTestCases = 0

numOfTestCases = int(file1.readline())
a = []
results = []
for i in xrange(numOfTestCases):
	a = file1.readline()
	numChosen = int(a)
	s1 = Set()
	s2 = Set()
	for x in xrange(4):
		if x == numChosen-1:
			word1 = file1.readline()
			for word in word1.split():
				s1.add(int(word.rstrip("\n ")))
		else:
			a = file1.readline()
	a = file1.readline()
	numChosen = int(a)
	for x in xrange(4):
		if x == numChosen-1:
			word1 = file1.readline()
			for word in word1.split():
				s2.add(int(word.rstrip("\n ")))
		else:
			file1.readline()
	if len(s1&s2)>1:
		results.append("Bad magician!")
	elif len(s1&s2) == 1:
		results.append(list(s1&s2)[0])
	elif len(s1&s2)==0:
		results.append("Volunteer cheated!")

for i in xrange(len(results)):
	print "Case #{0}: {1}".format(i+1,results[i])
