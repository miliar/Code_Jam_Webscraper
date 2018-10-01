import re

fr = open("input.txt", 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

numTests = lines[0].strip()
curTest = 0
curLine = 1

def getLine():
	global curLine
	global lines
	curLine += 1
	return lines[curLine-1]

while curTest < int(numTests):

	numBlocks = int(getLine())
	
	naomiBlocks = sorted(map(float, getLine().strip().split()))
	kenBlocks = sorted(map(float, getLine().strip().split()))
	
	warCounter = 0
	dWarCounter = 0
	
	kenBegDWarIdx = 0
	
	kenEndWarIdx = numBlocks - 1
	
	for i in range(numBlocks):
		reversei = (numBlocks-i) - 1
		if naomiBlocks[reversei] > kenBlocks[kenEndWarIdx]:
			warCounter += 1
		else:
			kenEndWarIdx -= 1
			
		if naomiBlocks[i] > kenBlocks[kenBegDWarIdx]:
			dWarCounter += 1
			kenBegDWarIdx += 1
		
	fw.write("Case #%d: %d %d\n" % (curTest+1, dWarCounter, warCounter))
	curTest += 1
					
fr.close()
fw.close()