import sys

inputStrings = open('A-large.in', 'r').read().splitlines()
caseNum = int(inputStrings[0])
outString = ""

lineNum = 1;
for case in range(1,caseNum+1):
    print(case)
    inData = inputStrings[lineNum].split(' ')
    destination = int(inData[0])
    horseCount = int(inData[1])


    lineNum += 1

    horseList = []
    for i in range(horseCount):
        horseData = inputStrings[lineNum].split(' ')

        #NOTE(ken): start position, speed
        otherHorse = [int(horseData[0]), int(horseData[1])]
        #TODO(ken): figure out how python creates fixed size arrays
        horseList.append(otherHorse);
        lineNum += 1

    longestFinishTime = 0.0
    for horse in horseList:
        distanceLeft = destination - horse[0]
        timeToFinish = float(distanceLeft) / horse[1]
        if timeToFinish > longestFinishTime:
            longestFinishTime = timeToFinish

    speed = destination / float(longestFinishTime)


    outString += "Case #" + str(case) + ": " + str(speed)
    if(case < caseNum):
        outString += "\n"

fileOut = open('A-large.out', 'w')
fileOut.write(outString)
fileOut.close()