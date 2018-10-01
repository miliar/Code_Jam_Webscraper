import sys

inf = open(sys.argv[1], 'r')
outf = open(sys.argv[1]+'.result', 'w')

def gcd(a,b):
    while b > 0: a,b = b, a%b
    return a

numCases = int(inf.readline())
cnt = 0
while cnt < numCases:
	numbers = []
	myarray = inf.readline().split(' ')
	numNumbers = int(myarray[0])
	i = 0
	while i < numNumbers:
		numbers.append(int(myarray[i+1]))
		i = i + 1
	numbers.sort()
	diffs=[]
	i = 0
	while i < len(numbers)-1:
		diffs.append(numbers[i+1]-numbers[i])
		i = i + 1
	mingcd = 0
	if len(diffs) == 1:
		mingcd = diffs[0]
	i = 0	
	while i < len(diffs)-1:
		currgcd = gcd(diffs[i],diffs[i-1])
		if mingcd == 0:
			mingcd = currgcd
		if mingcd > currgcd and currgcd != 0:
			mingcd = currgcd
		i = i + 1		
	leftBorder = (numbers[0]/mingcd)*mingcd
	if leftBorder == numbers[0]:
		result = 0
	else:	
		rightBorder = (numbers[0]/mingcd+1)*mingcd
		result = rightBorder - numbers[0]
#	print result	
#	i = 0
#	minDiff = 0
#	while i < numNumbers-1:
#		currDiff = numbers[i+1]-numbers[i]
#		if minDiff == 0:
#			minDiff = currDiff
#		if currDiff != 0 and minDiff > currDiff:
#			minDiff = currDiff
#		i = i + 1
#	if minDiff != 0:
#		leftBorder = (numbers[0]/minDiff)*minDiff
#		if leftBorder == numbers[0]:
#			result = 0
#		else:	
#			rightBorder = (numbers[0]/minDiff+1)*minDiff
#			result = rightBorder - numbers[0]
#	else:
#		result = 0
#		print result

	outf.write('Case #' + str(cnt+1) + ': ' + str(result) + '\n')
	cnt = cnt + 1
