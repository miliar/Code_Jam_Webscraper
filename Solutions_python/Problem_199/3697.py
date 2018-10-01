import sys
sys.setrecursionlimit(1000000)

def checkIfAllHappy(cakes):
	allUp = True
	for i in cakes:
		if i == '-':
			allUp = False
	return allUp

def recursiveFlip(cakes,n):
	print "test"

def opposite(side):
	if side == '+':
		return '-'
	elif side == '-':
		return '+'
	else:
		return '?'

def flipBasedOnArr(cakes,arr):
	temp = []
	for i in cakes:
		temp.append(i)
	for i in range(len(arr)):
		temp[arr[i]] = opposite(cakes[arr[i]])
	return ''.join(temp)

def getPositionArray(num, flip):
	arr = []
	a = 0
	while a < flip:
		arr.append(num + a)
		a += 1
	return arr

def getNegativePositionArray(num, flip):
	arr = []
	a = 0
	while a < flip:
		arr.append(num - a)
		a += 1
	return arr

def flipper(cakes,flip,n):
	#print cakes
	for i in range(len(cakes)):
		if cakes[i] == '-':
			if (i + flip)  <= len(cakes):
				cakes = flipBasedOnArr(cakes,getPositionArray(i,flip))
			else:
				cakes = flipBasedOnArr(cakes,getNegativePositionArray(i,flip))
			n += 1
			break
	
	if checkIfAllHappy(cakes):
		return n
	if n == (len(cakes) * flip):
		return "IMPOSSIBLE"
	
	return flipper(cakes,flip,n)

def flipperNonRecursive(cakes,flip,n):
	#print cakes
	for i in range(len(cakes)):
		if cakes[i] == '-':
			if (i + flip)  <= len(cakes):
				cakes = flipBasedOnArr(cakes,getPositionArray(i,flip))
			else:
				cakes = flipBasedOnArr(cakes,getNegativePositionArray(i,flip))
			n += 1
			i = 0
	
	if checkIfAllHappy(cakes):
		return n
	else:
		return "IMPOSSIBLE"


			
lines = open('input.txt').readlines()
q = 1
for line in lines:
	lineArr = line.split()
	if len(lineArr)  == 2:
		print "case #" + str(q)  + ": " + str(flipperNonRecursive(lineArr[0], int(lineArr[1]),0))
		q += 1
		
