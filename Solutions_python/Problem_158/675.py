import sys

def ominoComputation (sizeOmino, row, column):
    if row < column:
        row,column = column,row

    if sizeOmino == 1:
        return 'GABRIEL'

    if sizeOmino == 2:
        return 'GABRIEL' if ((row*column)%2) == 0 else 'RICHARD'

    if sizeOmino == 3:
        if (row*column)%3 != 0:
            return 'RICHARD'

        if row > 2 and column > 1:
            return 'GABRIEL'

        return 'RICHARD'

    if sizeOmino == 4:
        if (row*column)%4 != 0:
            return 'RICHARD'

        if row > 3 and column > 2:
            return 'GABRIEL'

        return 'RICHARD'

def processOminoFile (inputFileName, outputFileName):
    # Read the input file
    origFile = open(inputFileName, 'r')
    allFile = origFile.readlines()

    # Check the number of cases
    solvedCases = 0
    totalNumberCases = int(allFile.pop(0).strip())

    # Process the input file
    caseSolutions = []
    for line in allFile:
        cleanLine = line.strip()

        if len(cleanLine) > 0:
            print 'Processing case ' + str(solvedCases+1) + ' of ' + str(totalNumberCases)
            currentLineValues = cleanLine.split(' ')
            if len(currentLineValues) != 3:
                print 'Wrong format for list of omino parameters'
                print 'There were an incorrect number of components at the line: ' + cleanLine
                sys.exit()
            a = ominoComputation(int(currentLineValues[0]),int(currentLineValues[1]),int(currentLineValues[2]))
            caseSolutions.append('Case #' + str(solvedCases+1) + ': ' + str(a))
            solvedCases = solvedCases + 1

    if solvedCases != totalNumberCases:
        print 'Number of solved cases does not match the number of total cases'
        print 'Number of total cases is ' + str(totalNumberCases)
        print 'Number of solved cases is ' + str(solvedCases)

    # Open output file
    secondOutput = open(outputFileName, 'w')
    secondOutput.write('\n'.join(caseSolutions))
    secondOutput.close()

# Process the ovation input file to the program
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'Incorrect number of arguments given to the script.'
        print 'This script should be called with TWO parameters: python OminousOmino.py <inputFileName> <outputFileName>'
        sys.exit()
    else:
        print 'Processing Omino File'
        processOminoFile(sys.argv[1], sys.argv[2])

            
