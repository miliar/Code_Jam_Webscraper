fileID = open("B-small-attempt0.in","rt")

numberOfCases = int(fileID.readline())
whatToWrite = ''

for count in range(numberOfCases):
    case = count + 1

    whatToWrite += "Case #{0}: ".format(case)
    
    line = fileID.readline()
    line = line.strip('\n')
    line = line.split()
    
    combinations = int(line[0])
    combinationDict = {}
    
    if combinations > 0:
        combinationList = line[combinations:combinations+1]
        
        for eachCombo in combinationList:
            first = eachCombo[0] + eachCombo[1]
            second = eachCombo[1] + eachCombo[0]
            result = eachCombo[2]
            combinationDict[first] = result
            combinationDict[second] = result
        
            
    oppositions = int(line[combinations+1])
    oppositionList = []
    if oppositions > 0:
        start = combinations + 2
        finish = start + oppositions
        oppositionList = line[start:finish]         

    cast = line[-1]
    invoke = [cast[0]]
    lastElement = cast[0]
    
    for x in range(1,len(cast)):
        if len(invoke) > 0:
            lastElement = invoke[-1]
            
        invoke.append(cast[x])

        lastTwoElements = lastElement + cast[x]

        if combinationDict.has_key(lastTwoElements):
            invoke.pop(-1)
            invoke.pop(-1)
            invoke.append(combinationDict[lastTwoElements])
            lastElement = ''
            
        for eachOpp in oppositionList:
            firstOpp = eachOpp[0]
            secondOpp = eachOpp[1]
            if firstOpp in invoke and secondOpp in invoke:
                invoke = []
                lastElement = ''
            else:
                lastElement = cast[x]
                
    whatToWrite += '['
        
    for y in range(len(invoke)):
        whatToWrite = whatToWrite + invoke[y] + ", "

    whatToWrite = whatToWrite.strip(', ')
    whatToWrite += ']\n'

fileID.close()

fileID = open("output.in","wt")
fileID.write(whatToWrite)
fileID.close()










        
