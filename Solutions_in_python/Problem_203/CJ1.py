t = int(raw_input())

def isAllEmpty(oneLine):
	return set(oneLine) == set([None])

def processOneLine(oneLine):
	initial = findFirst(oneLine)
	out = []
	for x in oneLine:
		if x != '?' and x != initial:
			initial = x
		out.append(initial)
	return out

def findFirst(oneLine):
	for x in oneLine:
		if x != '?':
			return x

def findFirstLine(oneCake):
	for i, x in enumerate(oneCake):
		if set(x) != set(['?']):
			return 	i

def processOneCake(oneCake):
	firstNoEmptyLine = findFirstLine(oneCake)
	tempCake = [processOneLine(x) for x in oneCake]
	tempCake = [tempCake[firstNoEmptyLine] for i in range(firstNoEmptyLine)] + tempCake[firstNoEmptyLine:]
	for i, x in enumerate(tempCake):
		if isAllEmpty(x):
			tempCake[i] = tempCake[i - 1]
	return tempCake


for i in xrange(1, t + 1):
	rawCake = []
	n, m = [int(x) for x in raw_input().split()]
	for j in xrange(1, n + 1):
		rawCake += [list(raw_input().split()[0])]		
	print "Case #{}: ".format(i)
	newCake =  processOneCake(rawCake)
	for x in newCake:
		print ''.join(x)