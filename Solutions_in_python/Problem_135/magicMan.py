from sys import stdin

def lineToNumList(line):
    list = []
    line = line.split(' ')
    for num in line:
        list.append(int(num))
    return list

def getLine(lineNum):
    res = []
    for i in range(1,5):
        lineIn = lineToNumList(stdin.readline())
        if (i == lineNum):
            res = lineIn
            # print("Res: " + str(res))
    return res

def printCase(poss, testNum):
    if (len(poss) == 0):
        print("Case #" + str(testNum) + ": Volunteer cheated!")
    elif (len(poss) > 1):
        print("Case #" + str(testNum) + ": Bad magician!")
    else:
        print("Case #" + str(testNum) + ": " + str(poss[0]))

def main():
    numTests = 0
    line1 = []
    line2 = []
    testCases = int(input())
    while(numTests < testCases):
        numTests += 1
        guess1 = int(input())
        line1 = getLine(guess1)
        guess2 = int(input())
        line2 = getLine(guess2)
        possibilities = list(set(line1).intersection(line2))
        printCase(possibilities, numTests)

main()