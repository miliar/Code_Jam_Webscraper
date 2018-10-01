#!/usr/bin/python -u

import sys
import itertools

#----------------------------------------------------------------------
def findFirstBlue(R,C,matrix, startR = 0, startC = 0):

    row = startR
    col = startC

    while True:
        if matrix[row][col] == '#':
            return row,col

        col += 1
        if col >= C:
            col = 0
            row += 1

            if row >= R:
                return None, None

#----------------------------------------------------------------------


def subSolve(R,C,matrix, rowOffs, colOffs, initRow, initCol):

    # starting at initRow and initCol, try to put red tiles
    pass


def solveRegion(R,C, matrix):
    # cound number of blue tiles
    numBlueTiles = sum([ line.count('#') for line in matrix ])
    if numBlueTiles % 4 != 0:
        return None

    if numBlueTiles == 0:
        return matrix
        # print >> sys.stderr,"warning, internal error"

    startRow = 0
    startCol = 0

    solution = [ [ '.'] * C for r in range(R) ]

    while startRow != None:
        # find a blue tile (there must be at leat one)
        startRow, startCol = findFirstBlue(R,C, matrix, startRow, startCol)

        if startRow == None:
            # no blue tiles left
            return solution

        # try to cover this blue tile
        # try to cover starting from this. No need to shift offsets
        # can't shift to the left (there is no blue tile there)
        # can't shift to the right (must cover this tile)
        # can't shift to the top (there is no tile there)
        # can't shift to the bottom (must cover this tile)

        if startCol + 1 >= C:
            return None
        
        if startRow + 1 >= R:
            return None

        for dr,dc, char in ((0,0, '/'),
                            (0,1, '\\'),
                            (1,0, '\\'),
                            (1,1, '/')
                            ):
            if matrix[startRow + dr][startCol + dc] != '#':
                # can't put a red tile here
                return None

            matrix[startRow + dr][startCol + dc] = '.'

            solution[startRow + dr][startCol + dc] = char

        


    
    return solution

# def solve(R,C,matrix):
# 
#     numBlueTiles = sum([ line.count('#') for line in matrix ])
#     if numBlueTiles % 4 != 0:
#         return None
# 
#     # find regions
#     regions = []
# 
#     remainingTiles = numBlueTiles
# 
#     nextRow = 0
#     nextCol = 0
# 
#     while True:
#         thisRegion = [ [ '.'] * C for r in range(R) ]
# 
#         if matrix[nextRow][nextCol] != '#':
#             nextCol += 1
#             if nextCol >= C:
#                 nextCol = 0
#                 nextRow += 1
#                 if nextRow >= R:
#                     break
# 
#         # flood fill
#         remainingPoints = [ (nextRow, nextCol) ]
#         while remainingPoints:
#             row, col = remainingPoints.pop(0)
#             thisRegion[row][col] = '#'
#             matrix[row][col] = '.'
# 
#             # check neighbours (but only across edges)
#             for dr, dc in ((-1,0), (+1,0), (0,-1),(0,+1)):
# 
#                 newRow = row + dr
#                 newCol = col + dc
# 
#                 if newRow < 0 or newRow >= R:
#                     continue
#                 
#                 if newCol < 0 or newCol >= C:
#                     continue
# 
#                 if matrix[newRow][newCol] == '#':
#                     remainingPoints.append((newRow, newCol))
# 
#         regions.append(thisRegion)
# 
#     overallSolution = [ [ '.' ] * C for r in range(R) ]
# 
#     for region in regions:
#         sol = solveRegion(R,C, region)
# 
#         if sol == None:
#             return None
# 
#         # copy over red tiles
#         for row in range(R):
#             for col in range(C):
#                 if sol[row][col] != '.':
#                     overallSolution[row][col] = sol[row][col]
# 
#     return overallSolution
#     
# 
#     pass
    
#----------------------------------------------------------------------

# def solveBruteForce(R,C,matrix):
# 
#     # cound number of blue tiles
#     numBlueTiles = sum([ line.count('#') for line in matrix ])
#     if numBlueTiles % 4 != 0:
#         return None
# 
#     while True:
#         # find a blue tile
#         for row in range(R):
#             for col in range(C):
#                 if matrix[row][col] == '#':
# 
#                     # try to cover starting from this one
#                     
        
    


#----------------------------------------------------------------------

#----------------------------------------------------------------------
# main
#----------------------------------------------------------------------

T = int(sys.stdin.readline())

for case in range(1,T+1):

    R,C = [ int(x) for x in sys.stdin.readline().split('\n')[0].split(' ')  ]

    matrix = []
    for i in range(R):
        matrix.append(sys.stdin.readline().split('\n')[0])

        # convert to single characters
        matrix[-1] = list(matrix[-1])

    # if case != 19:
    #     continue
    # 
    # for line in matrix:
    #     print "".join(line)

    sol = solveRegion(R,C,matrix)


    print "Case #%d:" % case

    if sol == None:
        print "Impossible"
    else:
        for line in sol:
            print "".join(line)

