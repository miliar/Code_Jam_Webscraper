filename = "A-large.in"
outputname = filename + "out.txt"

inFile = open(filename, 'r')
outFile = open(outputname, 'w')

numCases = int(inFile.readline())

def getSingleCost(positions):
    answer = len(positions)
    positions = [1] + positions
    for i in range(len(positions)-1):
        answer += abs(positions[i] - positions[i+1])
    return answer

for i in range(numCases):
    nextLine = inFile.readline().split()
    numButtons = int(nextLine[0])
    orangeList = []
    blueList = []
    colorList = []
    for j in range(numButtons):
        colorList += [nextLine[j*2 + 1]]
        if nextLine[j*2 + 1] == 'O':
            orangeList += [int(nextLine[j*2 + 2])]
        else:
            blueList += [int(nextLine[j*2 + 2])]

    counter = 0
    blueLoc = 1
    orangeLoc = 1
    if len(blueList) == 0:
        counter = getSingleCost(orangeList)
    elif len(orangeList) == 0:
        counter = getSingleCost(blueList)
    else:
        nextBlueLoc = blueList[0]
        nextOrangeLoc = orangeList[0]
        while True:
            counter += 1
            blueMoved = False
            orangeMoved = False
            # Check if you can push a button
            if nextBlueLoc == blueLoc and colorList[0] == 'B':
                colorList.pop(0)
                blueMoved = True
                blueList.pop(0)
                if len(blueList) == 0:
                    nextBlueLoc = blueLoc
                else:
                    nextBlueLoc = blueList[0]
            elif nextOrangeLoc == orangeLoc and colorList[0] == 'O':
                colorList.pop(0)
                orangeMoved = True
                orangeList.pop(0)
                if len(orangeList) == 0:
                    nextOrangeLoc = orangeLoc
                else:
                    nextOrangeLoc = orangeList[0]

            # If you need to move to get to your next one, do so.
            if not blueMoved and blueLoc != nextBlueLoc:
                if blueLoc < nextBlueLoc:
                    blueLoc += 1
                else:
                    blueLoc -= 1
            if not orangeMoved and orangeLoc != nextOrangeLoc:
                if orangeLoc < nextOrangeLoc:
                    orangeLoc += 1
                else:
                    orangeLoc -= 1

            if len(colorList) == 0:
                break
            
    outFile.write("Case #" + str(i+1) + ": " + str(counter) + "\n")
            

inFile.close()
outFile.close()
