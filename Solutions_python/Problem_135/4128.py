import sys

filepath = sys.argv[1]
file = open(filepath, 'r')

testCases = int(file.readline())

for i in range(1, testCases + 1):

	first = int(file.readline())
	firstRound = []
	for r in range(4):
		s = file.readline()
		l = [int(e) for e in s.split(" ")]
		firstRound.append(l)
	
	second = int(file.readline())
	secondRound = []
	for r in range(4):
		s = file.readline()
		l = [int(e) for e in s.split(" ")]
		secondRound.append(l)

	firstSet = set(firstRound[first - 1])
	secondSet = set(secondRound[second - 1])
	
	intersect = firstSet.intersection(secondSet)
	
	size = len(intersect)
	
	if (size == 0) :
		print "Case #%d: Volunteer cheated!" % i
	elif (size == 1):
		print "Case #{0}: {1}".format(i, intersect.pop())
	else:
		print "Case #%d: Bad magician!" % i