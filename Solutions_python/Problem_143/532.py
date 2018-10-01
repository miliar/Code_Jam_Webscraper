import re

fr = open("input.txt", 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

numTests = int(lines[0].strip())
curTest = 0
curLine = 1

def getLine():
	global curLine
	global lines
	curLine += 1
	return lines[curLine-1].rstrip()
	
def getMult():
	return getLine().strip().split()

def getMultInt():
	return map(int, getMult())
	
def getMultFloat():
	return map(float, getMult())

	
while curTest < numTests:	
	
	# ...
	A, B, K = getMultInt()
	
	total = 0
	
	# Can't think of a fast way to do this yet...
	for i in range(A):
		for j in range(B):
			n = i&j
			if n < K:
				total += 1
		
	s = str(total)
	fw.write("Case #%d: %s\n" % (curTest+1, s))
	curTest += 1
					
fr.close()
fw.close()