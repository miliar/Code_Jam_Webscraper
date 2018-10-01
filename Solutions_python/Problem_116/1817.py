"""
    Problem A. Tic-Tac-Toe-Tomek
"""
import sys

sOw = 'O won'
sXw = 'X won'
sD = 'Draw'
sGHNC = 'Game has not completed'

# Solve 4x4 tic tac toe (row, column or a diagonal) with 'T' as wild card
def solve(array):
    result = solveRow(array)
    if result != None:
        return result

    result = solveColumn(array)
    if result != None:
        return result

    result = solveDiagonal(array)
    if result != None:
        return result

    result = checkBlank(array)
    if result != None:
        return result

    return sD

def solveRow(array):
    result = None
    for x in array:
        co = 0
        cx = 0
        ct = 0
        for y in x:
            if y == 'X':
                cx =  cx + 1
            elif y == 'O':
                co =  co + 1
            elif y == 'T':
                ct =  ct + 1
        if (cx+ct) == 4:
            return sXw
        if (co+ct) == 4:
            return sOw

def solveColumn(array):
    result = None
    for t in range(4):
        co = 0
        cx = 0
        ct = 0
        for x in array:
            y = x[t]
            if y == 'X':
                cx =  cx + 1
            elif y == 'O':
                co =  co + 1
            elif y == 'T':
                ct =  ct + 1
        if (cx+ct) == 4:
            return sXw
        if (co+ct) == 4:
            return sOw

def solveDiagonal(a):
    result = None
    newarray = [ [a[0][0],a[1][1],a[2][2],a[3][3]] , [a[0][3], a[1][2], a[2][1], a[3][0]]]
    for t in newarray:
        co = 0
        cx = 0
        ct = 0
        for y in t:
            if y == 'X':
                cx =  cx + 1
            elif y == 'O':
                co =  co + 1
            elif y == 'T':
                ct =  ct + 1
        if (cx+ct) == 4:
            return sXw
        if (co+ct) == 4:
            return sOw

def checkBlank(array):
    result = None
    cdot = 0
    for x in array:
        for y in x:
            if y == '.':
                cdot =  cdot + 1
    if cdot > 0:
        return sGHNC
    else:
        return None

if  __name__ == '__main__':
    numberCases = int(raw_input()) 
    i = 0 
    while i < numberCases:
        i = i+1
        tic = [None]*4
        for x in range(4):
            line = raw_input()
            arLine = list(line)
            tic[x] = arLine
        raw_input()
        #sys.stdout.write('tic %s\n' % str(tic) )
        answer = solve(tic)
        sys.stdout.write('Case #%d: %s\n' % (i, answer) )
