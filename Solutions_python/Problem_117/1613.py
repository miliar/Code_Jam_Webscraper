'''
Created on 13.04.2013

@author: MrCube
'''
from copy import copy, deepcopy


def cutRow(height, res, field, N, M, i):
    tmpRes = deepcopy(res)
    for j in range(0, M):
        if(field[i][j] > height):
            # cant cut remain old
            return res
        else:
            # can cut
            tmpRes[i][j] = height
    return tmpRes

def cutRowFromRight(height, res, field, N, M, i):
    tmpRes = deepcopy(res)
    for j in reversed(range(0, M)):
        if(field[i][j] > height):
            # cant cut remain old
            return res
        else:
            # can cut
            tmpRes[i][j] = height
    return tmpRes

def cutColumn(height, res, field, N, M, j):
    tmpRes = deepcopy(res)
    for i in range(0, N):
        if(field[i][j] > height):
            # cant cut remain old
            return res
        else:
            # can cut
            tmpRes[i][j] = height
    return tmpRes

def cutColumnFromBottom(height, res, field, N, M, j):
    tmpRes = deepcopy(res)
    for i in reversed(range(0, N)):
        if(field[i][j] > height):
            # cant cut remain old
            return res
        else:
            # can cut
            tmpRes[i][j] = height
    return tmpRes

def findNextMax(maxi, field, N, M):
    nextMax = -1
    for i in range(0, N):
        for j in range(0, M):
            val = field[i][j]
            if (field[i][j] > nextMax) and (field[i][j] < maxi):
                nextMax = val
    return nextMax

def cutToNextMax(maxi, res, field, N, M):
    for i in range(0,N):
        res =cutRow(maxi, res, field, N, M, i)
    for j in range(0,M):
        res = cutColumn(maxi, res, field, N, M, j)
    for i in range(0,N):
        res =cutRowFromRight(maxi, res, field, N, M, i)
    for j in range(0,M):
        res = cutColumnFromBottom(maxi, res, field, N, M, j)
    return res
    
def processField(field, N, M):
    # find first max value
    maxi = 100
    for i in range(0, N):
        for j in range(0, M):
            val = field[i][j]
            if (field[i][j] > maxi):
                maxi = val
                
    # assume that first max val can be cut
    res = []
    for i in range(0, N):
        row = []
        for j in range(0, M):
            row.append(maxi)
        res.append(row)
        
    # cut till all max values were cut
    nextMax = findNextMax(maxi, field, N, M)
    while nextMax > 0:
        res = cutToNextMax(nextMax, res, field, N, M)
        nextMax = findNextMax(nextMax, field, N, M)
    
    return res
        

'''input = """1
5 9
2 2 1 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2
"""
'''
import sys

input = open(sys.argv[1], "r").read()

input = input.splitlines()
numOfTests = int(input[0])
input = input[1:]

for test in range(1, numOfTests + 1):
    size = input[0].split(' ')
    N = int(size[0])
    M = int(size[1])
    input = input[1:]
    
    field = []
    for i in range(0, N):
        row = []
        for j in input[i].split(' '):
            row.append(j)
        field.append(row)
        
    '''for i in range(0, N):
        row = []
        for j in range(0, M):
            row.append(input[i][j])
        field.append(row)'''
    input = input[N:]
    
    res = processField(field, N, M)
    
    # compare res and field
    isValid = True
    for i in range(0, N):
        for j in range(0,M):
            if res[i][j]!=field[i][j]:
                isValid = False
            
    print "Case #%s: %s" %(test, "YES" if isValid else "NO")
                
            
