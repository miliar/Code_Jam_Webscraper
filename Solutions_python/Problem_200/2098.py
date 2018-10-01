import sys

def IsTidy(numArray):
    result = True
    currentNum = numArray[0]
    for num in numArray:
        if(num < currentNum):
            result = False
            break
        currentNum = num
    return result

def WorkOnArray(numArray, maxNumToConsider):
    largestNum = 0
    largestNumIndex = 0
    for i, num in enumerate(numArray):
        if(num > largestNum and num <= maxNumToConsider):
            largestNum = num
            largestNumIndex = i

    #NOTE(ken): not the last digit
    if(largestNumIndex < len(numArray) - 1):
        lower = False
        for i in range(largestNumIndex+1, len(numArray)):
            if numArray[i] < numArray[largestNumIndex]:
                lower = True
                break
        if lower:
            numArray[largestNumIndex] = numArray[largestNumIndex] - 1
            for i in range(largestNumIndex+1, len(numArray)):
                numArray[i] = 9
        else:
            maxNumToConsider = maxNumToConsider - 1
    else:
        #NOTE(ken): The last digit, must be an issue with a high order number
        maxNumToConsider = maxNumToConsider - 1

    return numArray, maxNumToConsider



inputStrings = open('B-large.in', 'r').read().splitlines()
caseNum = int(inputStrings[0])
outString = ""

lineNum = 1;
for case in range(1,caseNum+1):
    lastCountedNum = int(inputStrings[lineNum])
    lineNum += 1

    maxNumToConsider = 9
    lastTidyNum = 0
    if(lastCountedNum < 10):
        lastTidyNum = lastCountedNum
    else:
        lastCountedArray = list(map(int,str(lastCountedNum)))
        #TODO(ken): check if already tidy
        while (not IsTidy(lastCountedArray)) and maxNumToConsider > 0:
            lastCountedArray, maxNumToConsider = WorkOnArray(lastCountedArray, maxNumToConsider)

        lastTidyNum = int(''.join(map(str, lastCountedArray)))

    outString += "Case #" + str(case) + ": " + str(lastTidyNum)
    if(case < caseNum):
        outString += "\n"


fileOut = open('B-large.out', 'w')
fileOut.write(outString)
fileOut.close()