
def GetResult(rows):
	for i in range(0,len(rows)):
		for j in range(0,len(rows[i])):
			rows[i][j]=int(rows[i][j])

	columns=[]
	nrColumns=len(rows[0])
	values=[]
	for i in range(0,nrColumns):
		columns.append([])
		for row in rows:
			columns[i].append(row[i])
			if row[i] not in values:
				if row[i]>100 or row[i]<1:
					print "Wrong height"
					return 0
				values.append(row[i])

	minVal=min(values)

	for row in rows:
		if minVal in row:
			
			if len(set(row))==1:
				pass
			else:
				indices = [i for i, x in enumerate(row) if x == minVal]
				for i in indices:
					if  len(set(columns[i]))==1 and minVal in columns[i]:
						pass
					else:
						return 0

		
	return 1




fileName=raw_input("Name of the input file or full path:  ")
fileHandle=open(fileName,'r')
allLines=[]
for line in fileHandle:
	allLines.append(line.rstrip())
fileHandle.close()

curLine=0
nrCases=int(allLines[curLine])
curLine+=1

allCases=[]
for i in range(1,nrCases+1):
	nrRows=int(allLines[curLine].split()[0])
	oneCase=[]
	for line in allLines[curLine+1:curLine+nrRows+1]:
		oneCase.append(line.split())

	allCases.append(oneCase)
	curLine+=nrRows+1





results={0:"NO", 1:"YES"}
outputFile=open(fileName.split('.')[0]+'.out','a')
count=0
for c in allCases:
	count+=1
	if count>1:
		outputFile.write('\n')
	outputFile.write('Case #'+str(count)+': '+results[GetResult(c)])
outputFile.close()