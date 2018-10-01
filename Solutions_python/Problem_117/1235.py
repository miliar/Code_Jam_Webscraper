import sys

def readTestCase(fileContents, startIndex):
    (rows, cols) = (int(x) for x in fileContents[startIndex].split(' '))
    startIndex += 1

    mat = []
    for r in range(rows):
        mat.append([int(x) for x in fileContents[startIndex].split(' ')])
        startIndex += 1

    return (startIndex, mat, rows, cols)

# Get the input file name
inputFileName = sys.argv[1]

# Read file contents
with open(inputFileName) as f:
    contents = [line.strip() for line in f.readlines()]

# Get number of inputs
lineNum = 0;
numInputs = int(contents[lineNum])
lineNum += 1

for i in range(numInputs):
    # Read in input
    (lineNum, mat, rows, cols) = readTestCase(contents, lineNum)

    # Calculate max per row and col
    rowMaxes = []
    colMaxes = []

    for r in range(rows):
        rowMaxes.append(max(mat[r]))

    for c in range(cols):
        colMaxes.append(max([row[c] for row in mat]))

    isValid = True
    for r in range(rows):
        rowMax = rowMaxes[r]
        for c in range(cols):
            colMax = colMaxes[c]
            val = mat[r][c]
            if val < rowMax and val < colMax:
                isValid = False
                break

        if not isValid:
            break
    
    if isValid:
        print "Case #%d: YES" % (i+1)
    else:
        print "Case #%d: NO"  % (i+1)


