import fileinput
import math

def readFile(filename = 'c:\python27\GCJ\sample.txt', inputInts=[]):

	for line in fileinput.input(filename):
		inputInts.append(map(int, line.strip().split(' ')))
	return inputInts
	
def writeFile(filename = 'c:\python27\GCJ\output.txt', answer=[]):
	f = open(filename, 'w')
	i=0
	for j in answer:
		f.write( "Case #" +str(i+1) +": " +j +"\n")
		i=i+1
	f.close()
	
	
def findFairnSquare( startroot = 1,endroot = 100):
	count=0
	for j in range(startRoot,endRoot+1):
		if ( j == int(str(j)[::-1]) ):
			if (j*j == int(str(j*j)[::-1])):
				count = count+1
	return count

	
###################################################
#main
inputAr=readFile()
N = inputAr[0][0]
answern=[]
answers=[]

for i in range(1,N+1):
	startNo=inputAr[i][0]
	endNo=inputAr[i][1]
	startRoot=int(math.ceil(math.sqrt(startNo)))
	endRoot=int(math.floor(math.sqrt(endNo)))
	answern.append(findFairnSquare(startRoot,endRoot))

for i in answern:
	answers.append(str(i))
	
writeFile('c:\python27\GCJ\output.txt',answers)