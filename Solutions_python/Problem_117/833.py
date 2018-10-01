import sys
import numpy as np


def solveCase(C, lawn):

    colMax = np.amax(lawn, 0)
    rowMax = np.amax(lawn, 1)

    for i in range(len(rowMax)):
        for j in range(len(colMax)):
            if lawn[i,j] < rowMax[i] and lawn[i,j] < colMax[j]:
                return 'Case #%i: %s' % (C, 'NO')
    
    return 'Case #%i: %s' % (C, 'YES')


def processFile(inputFile, outputFile):
    fileIn = open(inputFile, 'rU')
    fileOut = open(outputFile, 'w')

    cases = int(fileIn.readline().strip())
    C = 0
    while C < cases:
        C += 1
        row = fileIn.readline().strip().split(' ')
        lawnRows = int(row[0])
        lawnCols = int(row[1])
        lawn = []
        for i in range(lawnRows):
            lawnRow = []
            row = fileIn.readline().strip().split(' ')
            for j in range(len(row)):
                lawnRow.append(int(row[j]))
            lawn.append(lawnRow)
        lawn = np.array(lawn)
        
        result = solveCase(C, lawn)
        
        fileOut.write(result + '\n')

    fileIn.close()
    fileOut.close()
            

processFile('B-large.in', 'B-large.out')
