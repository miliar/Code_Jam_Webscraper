fIn = open("input.in","r")
fOut = open("output.txt","w")
numberOfCaseStr = fIn.readline()
numberOfCaseStrSplit = numberOfCaseStr.split()
numberOfCases = int(numberOfCaseStrSplit[0])
for time in range(numberOfCases):
    rowStr1 = fIn.readline()
    rowStrSplit1 = rowStr1.split()
    rowNumber1 = int(rowStrSplit1[0])
    rowElement1 = []
    for i in range(rowNumber1-1):
        irrelevant = fIn.readline()
    relevant = fIn.readline()
    elements = relevant.split()
    for i in elements:
        rowElement1.append(i)
    for j in range(4-rowNumber1):
        irrelevant = fIn.readline()
    rowStr2 = fIn.readline()
    rowStrSplit2 = rowStr2.split()
    rowNumber2 = int(rowStrSplit2[0])
    rowElement2 = []
    for i in range(rowNumber2-1):
        irrelevant = fIn.readline()
    relevant = fIn.readline()
    elements = relevant.split()
    for i in elements:
        rowElement2.append(i)
    for j in range(4-rowNumber2):
        irrelevant = fIn.readline()
    
    sameNumber = []
    for x in rowElement1:
        for y in rowElement2:
            if x == y:
               sameNumber.append(x)
               number = x
    
    if len(sameNumber) == 1:
        line = "Case #{}: ".format(time+1) + str(number)
        fOut.write(line)
        fOut.write("\n")
    elif len(sameNumber) > 1:
        line = "Case #{}: Bad magician!".format(time+1)
        fOut.write(line)
        fOut.write("\n")
    elif len(sameNumber) == 0:
        line = "Case #{}: Volunteer cheated!".format(time+1)
        fOut.write(line)
        fOut.write("\n")
fIn.close()
fOut.close()
