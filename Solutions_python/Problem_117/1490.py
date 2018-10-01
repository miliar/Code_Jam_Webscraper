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
		[n,m] = contentFile.pop(0).replace('\n', '').split(' ')
		testCase = []
		
		for y in range(int(n)):
			line = contentFile.pop(0).replace('\n', '').split(' ')
			testCase.append(line)
			
		testCaseList.append(testCase)

	return testCaseList
	

def testCell(cellValue, line) :
	line = sorted(line)
	result = ''
	if (line[-1] > cellValue):
		result = 'NO'
	else :
		result = 'YES'
		
	return result
		
# Test one case
def testGrid(grid):

	firstResult = []

	for line in grid :
		resultLine = []
		
		for cell in line :
			resultLine.append(testCell(cell, line))
		
		firstResult.append(resultLine)
	
	secondResult = []

	for line in zip(*grid) :
		resultLine = []
		
		for cell in line :
			resultLine.append(testCell(cell, line))
		
		secondResult.append(resultLine)
	
	secondResult = zip(*secondResult)

	n = len(firstResult)
	m = len(firstResult[0])
	
	for i in range(n):
		for j in range(m):
			if firstResult[i][j] == 'NO' and secondResult[i][j] == 'NO' :
				return 'NO'
			
	return 'YES'
		
# Test all case		
def testAllGrids(testCaseList):
	results = []
	for i in range(int(testCaseList.pop(0))):
		results.append(testGrid(testCaseList[i]))

	return results

# Generate output file
def generateOutputFile(fileName, results):
	f = open(fileName, 'w')
	i= 1
	for result in results:
		f.write('Case #' + str(i) + ': ' + result + '\n')
		i+=1
	f.close()
		

# Define a main() function
def main() :
	args = sys.argv[1:]
	
	if (len(args) != 2) :
		print 'usage: <sourceFile> <outputFile>'
		sys.exit(1)

 
	testCaseList = parseInput(args[0])
	results = testAllGrids(testCaseList)
	generateOutputFile(args[1], results)

# Standard boilerplate calling main
if __name__ == '__main__':
  main()
