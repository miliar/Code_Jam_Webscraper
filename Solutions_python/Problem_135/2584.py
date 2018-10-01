import sys

sys.stdin = open("A.in")

lines = [line.strip() for line in sys.stdin]


test = int(lines.pop(0))
curTest = 0
while curTest < test:
	startIndex = curTest * 10
	firstAnswer = int(lines[startIndex])
	firstList = set(lines[startIndex+firstAnswer].split())
	
	secondAnswer = int(lines[startIndex + 5])
	secondList = lines[startIndex + 5 + secondAnswer].split()
	
	answerList = list(firstList.intersection(secondList))
	
	listLen = len(answerList)
	if listLen == 1:
		print "Case #" + str(curTest + 1) + ": " + "".join(answerList)
	elif listLen > 1:
		print "Case #" + str(curTest + 1) + ": Bad magician!"
	else:
		print "Case #" + str(curTest + 1) + ": Volunteer cheated!"
	curTest += 1
