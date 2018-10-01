import sys

inFileName = r'C:\GCJ\QUA\Mag\A-small-attempt0.in' # sys.argv[1]
fileIn = open(inFileName)
fileOut = open(inFileName[:inFileName.rfind('.')] + '.out','w')

nCases=int(fileIn.readline())
for caseNum in range(nCases):
	line = fileIn.readline()

#Start of main logic
	RowNum = int(line)
	Row1 = []
	for idx in range(4):
		line = fileIn.readline()
		if idx == (RowNum - 1):
			Row1 = set(line.split())
	print(Row1)
	line = fileIn.readline()
	RowNum = int(line)
	Row2 = []
	for idx in range(4):
		line = fileIn.readline()
		if idx == (RowNum - 1):
			Row2 = set(line.split())

	print(Row1)
	final = Row1.intersection(Row2)
	print(final, len(final))
	if len(final) == 1:
		Ret = final.pop()
	elif len(final) == 0:
		Ret = 'Volunteer cheated!'
	elif len(final) > 1:
		Ret = 'Bad magician!'

	out = str(Ret)
#End of main logic

	print("Case #"+str(caseNum+1)+": "+out+'\n')
	fileOut.writelines("Case #"+str(caseNum+1)+": "+out+'\n')
	fileOut.flush()

fileIn.close()
fileOut.close()
