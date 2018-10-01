#!/usr/bin/python -tt
import sys

#Parse datas
def parseInput(fileName):
	f = open(fileName, 'rU')
	contentFile = f.readlines()
	f.close()
	
	nbCase = int(contentFile.pop(0))
	
	testCaseList = [nbCase]
	
	for i in range(nbCase):
		
		testCase = []
		
		for y in range(4):
			line = contentFile.pop(0)
			tup = (line[0], line[1], line[2], line[3])
			testCase.append(tup)
			
		testCaseList.append(testCase)
		
		#Remove empty line between each case
		contentFile.pop(0)

	return testCaseList
	
	
#Test a line
def testLine(tupLine) :
	assert len(tupLine) == 4, 'the tested line is incomplete'
	
	if '.' in tupLine :
		return 'Incomplete'
	elif 'X' in tupLine and 'O' in tupLine :
		return 'None'
	elif 'X' in tupLine :
		return 'X'
	else :
		return 'O'

#Test a case
def testCase(case):
	assert len(case) == 4, 'Parsing error'
	lineOne = case[0]
	lineTwo = case[1]
	lineThree = case[2]
	lineFour = case[3]
	
	caseResult = []
	
	caseResult.append(testLine(lineOne))
	caseResult.append(testLine(lineTwo))
	caseResult.append(testLine(lineThree))
	caseResult.append(testLine(lineFour))
	
	caseResult.append(testLine((lineOne[0], lineTwo[0], lineThree[0], lineFour[0])))
	caseResult.append(testLine((lineOne[1], lineTwo[1], lineThree[1], lineFour[1])))
	caseResult.append(testLine((lineOne[2], lineTwo[2], lineThree[2], lineFour[2])))
	caseResult.append(testLine((lineOne[3], lineTwo[3], lineThree[3], lineFour[3])))
		
	caseResult.append(testLine((lineOne[0], lineTwo[1], lineThree[2], lineFour[3])))
	caseResult.append(testLine((lineOne[3], lineTwo[2], lineThree[1], lineFour[0])))
		
	if 'X' in caseResult :
		return 'X won'
	elif 'O' in caseResult :
		return 'O won'
	elif 'Incomplete' in caseResult:
		return 'Game has not completed'
	else :
		return 'Draw'
		

def testAllCase(testCaseList) :
	result = []
	nbCase = testCaseList.pop(0)
	
	for i in range(nbCase):
		result.append(testCase(testCaseList[i]))
		
	return result


def generateOutputFile(fileName, results):
	f = open(fileName, 'w')
	i= 1
	for result in results:
		f.write('Case #' + str(i) + ': ' + result + '\n')
		i+=1
	f.close()
		

# Define a main() function
def main():
	args = sys.argv[1:]
	
	if (len(args) != 2) :
		print 'usage: <sourceFile> <outputFile>'
		sys.exit(1)

	testCaseList = parseInput(args[0])
	results = testAllCase(testCaseList)
	generateOutputFile(args[1], results)
 

# Standard boilerplate calling main
if __name__ == '__main__':
  main()
