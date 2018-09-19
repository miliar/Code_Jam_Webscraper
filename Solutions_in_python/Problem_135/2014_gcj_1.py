inputFile = open("A-small-attempt2.in", 'r')
outputFile = open("output.out", 'w')

lineCount = 0
rowNum = 0
caseNum = 0
choiceCount = 0
candidateList = []
while 1:
    line = inputFile.readline()
    
    lineCount = lineCount + 1
    if not line :
        break
    
    if lineCount == 1 :
        caseAmount = int(line.replace("\n", ""))
    elif lineCount % 5 == 2 :
        choiceRow = int(line.replace("\n", ""))
        choiceCount = choiceCount + 1
        if choiceCount % 2 == 1 :
            caseNum = caseNum + 1
        rowNum = 0
    elif lineCount != 1 and lineCount % 5 in [3,4,0,1] :
        rowNum = rowNum + 1
        if choiceRow == rowNum :
            if choiceCount % 2 == 1 :
                row = line.replace("\n", "").split(' ')
                candidateList = row
                
            else :
                row = line.replace("\n", "").split(' ')
                sameCount = 0
                for n in row :
                    if n in candidateList :
                        if sameCount >= 1 :
                            result = "Bad magician!"
                            break
                        sameCount = sameCount + 1
                        result = n
                if sameCount == 0 :
                    result = "Volunteer cheated!"
                    
                outputFile.write("Case #" + str(caseNum) + ": " + result + "\n")
                
inputFile.close()
outputFile.close()
