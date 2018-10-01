import sys

data = sys.stdin.readlines()
counter = 0
numTests = int(data[counter])
counter += 1

for i in xrange(numTests):
	numRow = int(data[counter])
	counter += numRow
	line1 = data[counter].split()
	counter += (4 - numRow) + 1

	numRow2 = int(data[counter])
	counter += numRow2
	line2 = data[counter].split()
	counter += (4 - numRow2) + 1

	setOfLines = set(line1) & set(line2)
	setIntersect = len(setOfLines)

	if setIntersect == 0:
		print "Case #" + str(i + 1) + ": Volunteer cheated!"

	elif setIntersect != 1:
		print "Case #" + str(i + 1) + ": Bad magician!"

	else:
		print "Case #" + str(i + 1) + ": " + str(setOfLines.pop())
