#only for small datasets
import sys
from time import time

def pow10(pow):
	res = 1;
	for i in range(pow):
		res*=10;
	return res;
	
def getDigitsCount1(number):
	return len(str(number))

def makeRecycled1(inputNum, digitsCount, symbolsToMove):
	inputStr = str(inputNum)
	resStr = inputStr[-symbolsToMove:] + inputStr[0:-symbolsToMove]
	return int(resStr)

	
def getRecycled(inputNum, minNumber, maxNumber, digitsCount):
	res = []
	#try remove
	if digitsCount == 1:
		return res;
	for symbolsToMove in range(1, digitsCount):
		recycled = makeRecycled1(inputNum, digitsCount, symbolsToMove)
		if not recycled in res:
			res.append(recycled)
	return res

def testRecycle(inputNum, recycledNum, minNumber, maxNumber, digitsCount):
	#try remove
	if inputNum > maxNumber: 
		return False
	#if less then min number then False
	if recycledNum < minNumber:
		return False
	#if greater then max number then False
	if recycledNum > maxNumber:
		return False
	#if less then already test
	#if same then this is not paired number 666 not pair for 666
	if recycledNum <= inputNum:
		return False
	return True

def doTest():
	splits = input.readline().split()
	aNumber =int(splits[0]);
	bNumber =int(splits[1]);
	aDigitsCount = getDigitsCount1(aNumber)
	bDigitsCount = getDigitsCount1(bNumber)
	if aDigitsCount != bDigitsCount:
		raise NameError("A and B digits count are not same")
	recycledCount = 0
	for curNum in range(aNumber, bNumber + 1):
		for curRecycled in getRecycled(curNum, aNumber, bNumber, aDigitsCount):
			if testRecycle(curNum, curRecycled, aNumber, bNumber, aDigitsCount):
				recycledCount+=1;
	return recycledCount

	
#sys.exit(0)

start = time()
	
if len(sys.argv) < 2:
	sys.exit("use argument; error")
	
input = open(sys.argv[1], "r")
output = open(sys.argv[1] + ".out", "w")

count = int(input.readline())

for curTestIndex in range(count):
	output.write("Case #%d: %d\n" % (curTestIndex+1, doTest()))

stop = time()
	
input.close()
output.close()    
print "success %f" % (stop-start)
	



	
	
