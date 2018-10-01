#!/usr/bin/python2.6 -tt
import sys

def solveMagician(inputFileName):
    inputFile = open(inputFileName, 'r')
    t = inputFile.readline()
    for i in range(int(t)):
        result = solveSet(inputFile)
        print "".join(['Case #', str(i + 1), ': ', result])
 
def solveSet(inputFile):
    firstRow = getRow(inputFile).split(' ')
    secondRow = getRow(inputFile).split(' ')
    overlap = []
    for x in secondRow:
        if x in firstRow:
            overlap.append(x)
        if len(overlap) > 1:
            break
    if len(overlap) > 1:
        return 'Bad magician!'
    elif len(overlap) < 1:
        return 'Volunteer cheated!'
    else:
        return str(overlap[0])

def getRow(inputFile):
    rowIndex = int(inputFile.readline())
    for i in range(rowIndex - 1):
        inputFile.readline()
    result = inputFile.readline().rstrip()
    for i in range(rowIndex, 4):
        inputFile.readline()
    return result


# Define a main() function that prints a greeting
def main():
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: sys.argv[0]')
        sys.exit(1)
    inputFileName = sys.argv[1]
    solveMagician(inputFileName)

# Standard boilerplate that calls the main function
if __name__ == '__main__':
    main()
