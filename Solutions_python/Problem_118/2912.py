from math import sqrt

def IsPol(number):
	if number != int(number):
		return False
	strg = str(int(number))
	n = len(strg)
#	print 'n=' + str(n) + strg
	for i in range(0,len(strg)):
#		print 'i=' + str(i) + 'n=' + str(n)
		if strg[i] != strg[n-i-1]:
			return False
	return True

inputFile = open('input.txt', 'r')
outputFile = open('output.txt', 'w')
T = int(inputFile.readline().strip())
caseIndex = 1
for eachLine in inputFile:
	splitted = eachLine.strip().split(' ')
	aStr = splitted[0]
	bStr = splitted[1]
	A = int(splitted[0])
	B = int(splitted[1])
	counter = 0
	for i in range(A, B+1):
		if IsPol(i) and IsPol(sqrt(i)):
			counter = counter + 1
	outputFile.write('Case #' + str(caseIndex) + ': ' + str(counter) + '\n')
	caseIndex = caseIndex + 1
inputFile.close()
outputFile.close() 