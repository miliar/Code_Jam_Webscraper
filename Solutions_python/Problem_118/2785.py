# 03_fair_aquare.py
import math

# Functions
def isPalindrome(numCheck):
	return (str(numCheck) == str(numCheck)[::-1])

def isEven(numInt):
	return numInt % 2 == 0

def splitStrInMiddle(strInp):
	lenNumInt = len(strInp)
	if (isEven(lenNumInt)):
		return [strInp[:(((lenNumInt-1)/2)+1)], strInp[(((lenNumInt-1)/2)+1):]]
	else:
		return [strInp[:((lenNumInt-1)/2)], strInp[(lenNumInt-1)/2],strInp[(((lenNumInt-1)/2)+1):]]

# def getStrMiddleChar(strInp):
# 	lenNumInt = len(strInp)
# 	return (strInp[lenNumInt/2-1] + strInp[lenNumInt/2]) if (isEven(lenNumInt)) else strInp[(lenNumInt-1)/2]

def getNextNumPalindrome(numInt):
	strInt = str(numInt)

	# For cases like 99 and 999
	if (strInt.count('9') == len(strInt)):
		numInt = numInt + 1
		strInt = str(numInt)

	answerStr = ""
	
	if (len(strInt) > 1):
		splitStr = splitStrInMiddle(strInt)
		firstHalfInt = int(splitStr[0])
		if isEven(len(strInt)):
			# Split in half and add to first part
			secondHalfInt = int(splitStr[1])
			firstHalf = firstHalfInt + 1 if (firstHalfInt <= secondHalfInt) else firstHalfInt
			answerStr = str(firstHalf) + str(firstHalf)[::-1]
		else:
			secondHalfInt = int(splitStr[2])
			middleInt = int(splitStr[1])
			if (firstHalfInt <= secondHalfInt): 

				if (int(splitStrInMiddle(strInt)[1]) < 9):
					answerStr =  str(firstHalfInt) + str(middleInt+1) + str(firstHalfInt)[::-1]
				else:
					answerStr = str(firstHalfInt+1) + "0" + str(firstHalfInt+1)[::-1]
			else: 
				answerStr =  str(firstHalfInt) + str(middleInt) + str(firstHalfInt)[::-1]

		return int(answerStr)
	else:
		return (numInt+1) if (numInt < 9) else 11

def isFairSquare(numInt):
	squareDbl = math.sqrt(numInt)
	squareCheck = ((int(squareDbl)*int(squareDbl)) == numInt)
	if (squareCheck):
		return (squareCheck and isPalindrome(int(squareDbl)))
	else: 
		return False


# Files management
f = open('./C-small-attempt1.in', 'r')
# f = open('./C-large.in', 'r')
# f = open('./C-task.in.txt', 'r')
#print f
fileLines = f.readlines()
f.close()
fo = open('./C-small-attempt1.out', 'w')
# fo = open('./C-large.out', 'w')
# fo = open('./C-task.out.txt', 'w')
fol = []
ranges = [0,10,[range(10)]]
# print ['getNextNumPalindrome', getNextNumPalindrome(99)]

# Data
stack = []
# output = []

cases = int(fileLines[0].strip())

for case in range(cases):
	result = []
	currentLine = fileLines[case+1].strip()
	currentLims = currentLine.split(' ')
	stack.append(currentLims)

	# Solving case
	start = int(currentLims[0].strip())
	finish = int(currentLims[1].strip())
	# print ['Lims', currentLims]
	curentNum = start if isPalindrome(start) else getNextNumPalindrome(start)

	#curentNum = getNextNumPalindrome(start)
	while (finish >= curentNum):
		if (isFairSquare(curentNum)):
			result.append(curentNum)
		curentNum = getNextNumPalindrome(curentNum)

	# print ['Result', result]
	outLine = "Case #" + str(case+1) + ": " + str(len(result))
	print outLine
	fol.append(outLine)

# Files management
for l in fol:
	fo.write(l + '\n')
fo.close()