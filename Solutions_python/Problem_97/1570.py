#!/usr/bin/python

f = open("C-small-attempt0.in", "r")

numberOfTestCases = 0
caseNumber = 1;
myOutputString = ""

for line in f:
	if numberOfTestCases==0 : numberOfTestCases = line.rstrip()
	else :
		myOutputString = "Case #" + str(caseNumber) + ": "
		caseNumber = caseNumber + 1
		iS = line.rstrip().split(" ")
		A = int(iS[0])
		B = int(iS[1])
		n = A
		total = 0
		while n <= int(B):
			i = str(n)
			for c in i[0:len(i)-1]:
				k = i[len(i)-1]+i[0:len(i)-1]
				if int(k) > n :
					if int(k) <= B : 
						total = total + 1
				i = i[len(i)-1]+i[0:len(i)-1] 
			n = n+1
		print myOutputString+str(total)