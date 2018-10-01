#!/usr/bin/pythin
import sys

A = open('B-small-attempt0.in')
T = int(A.readline())

output = open('mower.out', 'w')

def avg(A):
    return float(sum(A))/len(A)

def findmin(grid, minh):
    #find min
    realmin=101
    for row in grid:
        for i in row:
            if i < realmin:
                realmin = i
                #This is the smallest possible for this level
                #No point to continue looking
                if realmin == minh:
                    return realmin
    return realmin

def possible(grid, N, M, minh=1):
    clearedcols = set([])
    clearedrows = set([])
    
    #find min
    realmin = findmin(grid, minh)
    
    #Find routes
    for i in xrange(N):
        for j in xrange(M):
            tmp = grid[i][j]
            if tmp == realmin:
                if i in clearedrows or j in clearedcols:
                    continue
                else:
                    if avg(grid[i]) == realmin:
                        clearedrows.add(i)
                        break
                    elif avg([grid[k][j] for k in xrange(N)]) == realmin:
                        clearedcols.add(j)
                    else:
                        return False

    #find islands and run this again
    rowpairs = []
    start = -1
    for i in xrange(N):
        if i not in clearedrows:
            if start < 0:
                start = i
                continue
        elif start >= 0:
            rowpairs.append((start, i))
            start = -1
    if start >= 0:
        rowpairs.append((start, i+1))

    colpairs = []
    start = -1
    for i in xrange(M):
        if i not in clearedcols:
            if start < 0:
                start = i
                continue
        elif start >= 0:
            colpairs.append((start, i))
            start = -1
    if start >= 0:
        colpairs.append((start, i+1))
                
#    print [(i,j) for i in rowpairs for j in colpairs]
    
    for rowpair in rowpairs:
        for colpair in colpairs:
            tmpgrid = []
            for i in xrange(*rowpair):
                tmpgrid.append(grid[i][colpair[0]:colpair[1]])
            if not possible(tmpgrid, rowpair[1] - rowpair[0], colpair[1] - colpair[0], minh+1):
                return False
            
    return True
  
for i in xrange(T):
    N, M = map(int, A.readline().split(' '))
    
    grid = []
    for j in xrange(N):
        grid.append(map(int, A.readline().split()))

    if possible(grid, N, M):
        res = 'YES'
    else:
        res = 'NO'
          
    output.write('Case #{}: {}\n'.format(i+1, res))

#  output.write('Case #{}: {} {}\n'.format(1, 1, 1))

output.close()
