def readMap(fo):
    H, W = map(int, fo.readline().split())
    return [map(int, fo.readline().split()) for i in range(H)]

def markCell(matrix, labelMatrix, H, W, row, col, labelGen):
    if labelMatrix[row][col] != None:
        return labelMatrix[row][col]
    # otherwise, find the neighbor with lowest level
    dirctions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    currentMinimum = matrix[row][col]
    currentMinCellRow = row
    currentMinCellCol = col
    for dRow, dCol in dirctions:
        newRow = row + dRow
        newCol = col + dCol
        if 0 <= newRow < H and 0 <= newCol < W and \
                matrix[newRow][newCol] < currentMinimum:
            currentMinimum = matrix[newRow][newCol]
            currentMinCellCol = newCol
            currentMinCellRow = newRow
    if currentMinCellRow == row and currentMinCellCol == col:
        # is a sink, use the defaultLabel
        label = labelGen.next()
    else:
        # use the label of its lowest level nieghbor
        label = markCell(matrix, labelMatrix, H, W, currentMinCellRow, currentMinCellCol, labelGen)
    labelMatrix[row][col] = label
    return label

def makeLabelGenerator():
    count = 97
    while count <= 96+26:
        yield chr(count)
        count += 1

def solveMap(matrix):
    labelGen = makeLabelGenerator()

    H = len(matrix)
    W = len(matrix[0])

    labelMatrix = [[None]*W for r in range(H)]
    
    for row in range(H):
        for col in range(W):
            markCell(matrix, labelMatrix, H, W, row, col, labelGen)
    return labelMatrix

def printSolution(labelM):
    print "\n".join([" ".join(r) for r in labelM])
    
def main(f):
    fo = open(f, 'r')
    T = int(fo.readline())
    for i in range(T):
        print "Case #%d:" % (i+1)
        printSolution(solveMap(readMap(fo)))
    fo.close()
    
if __name__=='__main__':
    import sys
    main(sys.argv[1])
