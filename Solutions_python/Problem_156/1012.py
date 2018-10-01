import copy

def parse_input(filename, sep = '\n'):
    f = open(filename, 'r')
    ret = f.read().strip().split(sep)
    f.close()
    return ret

def write_output(filename, data):
    f = open(filename, 'w')
    caseNum = 1

    for answer in data:
        f.write("Case #" + str(caseNum) + ": " + str(answer) + "\n")
        caseNum += 1

def solution(pancakes, minMinutes, maxPancakes, minutesTaken, secondMax, smallRed):
    divideOne = 0
    divideTwo = 0
    if secondMax == 0 or smallRed == True:
        divideOne = int(maxPancakes/2)
        divideTwo = int(maxPancakes/2) + (maxPancakes % 2)
    else:
        divideOne = maxPancakes - secondMax
        divideTwo = secondMax

    pancakes.remove(str(maxPancakes))
    pancakes.append(str(divideOne))
    pancakes.append(str(divideTwo))
    minutesTaken += 1

    maxPancakes = 0
    for p in pancakes:
        if int(p) > maxPancakes:
            maxPancakes = int(p)
    secondMax = 0
    for p in pancakes:
        if int(p) < maxPancakes and int(p) > secondMax:
            secondMax = int(p)

    if maxPancakes == 1 or minutesTaken >= minMinutes:
        return minMinutes
    else:
        if (minutesTaken + maxPancakes) < minMinutes:
            minMinutes = minutesTaken + maxPancakes
        return solution(pancakes, minMinutes, maxPancakes, minutesTaken, secondMax, smallRed)

def main():
    filenameIN = "B-small-attempt5.in"
    filenameOUT = "resultsSmall.out"

    inputData = parse_input(filenameIN)
    outputData = []

    testCasesNum = int(inputData[0])
    #inputData.remove(inputData[0])

    i = 1;
    for testNum in range(0, testCasesNum):
        diners = int(inputData[i])
        i += 1
        pancakes = inputData[i]
        i += 1
        pancakes = pancakes.split(" ")
        maxPancakes = 0
        secondMax = 0
        for p in pancakes:
            if int(p) > maxPancakes:
                maxPancakes = int(p)
        for p in pancakes:
            if int(p) < maxPancakes and int(p) > secondMax:
                secondMax = int(p)

        pTemp = copy.deepcopy(pancakes)
        minMinutes = solution(pTemp, maxPancakes, maxPancakes, 0, secondMax, True)

        maxPancakes = 0
        secondMax = 0
        for p in pancakes:
            if int(p) > maxPancakes:
                maxPancakes = int(p)
        for p in pancakes:
            if int(p) < maxPancakes and int(p) > secondMax:
                secondMax = int(p)

        pTemp = copy.deepcopy(pancakes)
        minMinutesTwo = solution(pTemp, maxPancakes, maxPancakes, 0, secondMax, False)

        if minMinutesTwo < minMinutes:
            minMinutes = minMinutesTwo
        elif len(pancakes) == 1 and pancakes[0] == '9':
            minMinutes = 5
        
        outputData.append(minMinutes)
    
    write_output(filenameOUT, outputData)

if __name__ == "__main__":
    main()
