#! /usr/bin/env python3

lines = open("A-small-attempt0.in").readlines()

i = 0
testCases = int(lines[0])

while i < testCases:

	firstTryRowNum  = int(lines[1 + (i*10)])
	firstTryRow = set(lines[1 + (i*10) + firstTryRowNum].strip().split(" "))
	
	secondTryRowNum = int(lines[6 + (i*10)])
	secondTryRow = set(lines[6 + (i*10) + secondTryRowNum].strip().split(" "))

	i += 1

	intersectionValues = firstTryRow & secondTryRow
	if len(intersectionValues) == 1:
		print ("Case #%d: %s"%(i, intersectionValues.pop()))
	elif len(intersectionValues) == 0:
		print("Case #%d: Volunteer cheated!"%(i))
	else:
		print("Case #%d: Bad magician!"%(i))
	
