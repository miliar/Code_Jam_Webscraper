#!/usr/bin/python

def inBounds(matrix, r, c):
    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
        return False
    return True

def rise(matrix, r1, c1, r2, c2):
    if not (inBounds(matrix, r1, c1) and inBounds(matrix, r2, c2)):
        return False
    if matrix[r1][c1] < matrix[r2][c2]:
        return True
    return False

def highestInCol(matrix, c, val):
    for r in range(len(matrix)):
        if matrix[r][c] > val:
            return False
    return True

def highestInRow(matrix, r, val):
    for c in range(len(matrix[0])):
        if matrix[r][c] > val:
            return False
    return True

def checkPossible(lawn, r, c):
    if not inBounds(lawn, r, c):
        return True
    
#    possible = True
#    if rise(lawn, r, c, r, c-1) or rise(lawn, r, c, r, c+1):
#        possible = possible and highestInCol(lawn, c, lawn[r][c])
#    if rise(lawn, r, c, r-1, c) or rise(lawn, r, c, r+1, c):
#        possible = possible and highestInRow(lawn, r, lawn[r][c])
    
    possible = highestInCol(lawn, c, lawn[r][c]) or highestInRow(lawn, r, lawn[r][c])
    
    return possible

def debugPrint(matrix):
    for r in range(len(matrix)):
        print matrix[r]

########################################

T = int(raw_input())
for case in range(T):
    [N, M] = map(int, raw_input().split())
    lawn = []
    for row in range(N):
        lawn.append(map(int, raw_input().split()))

    possible = True
    for r in range(N):
        for c in range(M):
            if not checkPossible(lawn, r, c):
                possible = False
    
#    debugPrint(lawn)
    
    if possible:
        print 'Case #' + str(case+1) + ': YES'
    else:
        print 'Case #' + str(case+1) + ': NO'
    
    
