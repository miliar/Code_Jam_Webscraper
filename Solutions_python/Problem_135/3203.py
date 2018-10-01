import sys

#if len(sys.argv) > 1:

fileLocation = sys.argv[1].strip()
inputDataFile = open(fileLocation, 'r')

inputData = ''.join(inputDataFile.readlines())
inputDataFile.close()

outputDataFile = open(fileLocation+"_out", 'w')
	
#parse the input
lines = inputData.split('\n')

testcases = int(lines[0])

for a in range(0, testcases):
	
	answer1 = int(lines[1+a*10])
	print answer1
	
	firstRow = map(int, lines[1+a*10+answer1].split(' '))
	print firstRow
	
	answer2 = int(lines[1+a*10+5])
	print answer2
	
	secondRow = map(int, lines[1+a*10+5+answer2].split(' '))
	print secondRow
	
	results = list(set(firstRow) & set(secondRow))
	print results
	
	ret = "Case #"+str(a+1)+": "
	if len(results)==1:
		ret += str(results[0])
	elif len(results)==0:
		ret += "Volunteer cheated!"
	elif len(results)>1:
		ret += "Bad magician!"
	
	print ret
	outputDataFile.write(ret+"\n")

outputDataFile.close()