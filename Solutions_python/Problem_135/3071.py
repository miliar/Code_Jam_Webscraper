

def parse(filename):
    with open(filename) as f:
        cases = int(f.readline())
        problems = []
        for case in range(cases):
            firstGuess = int(f.readline())
            firstBoard = []
            for i in range(4):
                boardLine = f.readline()
                firstBoard.append(map(int, boardLine.split(" ")))
            secondGuess = int(f.readline())
            secondBoard = []
            for i in range(4):
                boardLine = f.readline()
                secondBoard.append(map(int, boardLine.split(" ")))

            problems.append([firstGuess, firstBoard, secondGuess, secondBoard])
        return problems


def solveProblem(problem):
    firstGuess, firstBoard, secondGuess, secondBoard = problem
    numbersFromFirstBoard = firstBoard[firstGuess - 1]
    dictFromFirstBoard = {}
    for number in numbersFromFirstBoard:
        dictFromFirstBoard[number] = True

    matchingNumber = 0
    matchingNumbers = 0

    numbersFromSecondBoard = secondBoard[secondGuess - 1]
    for number in numbersFromSecondBoard:
        if number in dictFromFirstBoard:
            matchingNumber = number
            matchingNumbers += 1

    if matchingNumbers == 0:
        return "Volunteer cheated!"
    if matchingNumbers > 1:
        return "Bad magician!"
    return matchingNumber


def parseAndPrint(filename):
    problems = parse(filename)
    case = 1
    for problem in problems:
        result = solveProblem(problem)
        print "Case #" + str(case) + ": " + str(result)
        case += 1


parseAndPrint("/Users/gcameron/Downloads/A-small-attempt0.in")