#!/bin/env python
import sys
def gen_indices(n):
    for i in range(n):
        yield [(i, j) for j in range(n)]
        yield [(j, i) for j in range(n)]
    yield [(i,i) for i in range(n)]
    yield [(i,n-i-1) for i in range(n)]

def checkO(char):
    return True if char == 'O' or char == 'T' else False

def checkX(char):
    return True if char == 'X' or char == 'T' else False

def solveb(b, case):
    for indices in gen_indices(4):
        if all(map(checkO, (b[i][j] for i, j in indices))):
            print('Case #%d: O won' % case)
            return
        if all(map(checkX, (b[i][j] for i, j in indices))):
            print('Case #%d: X won' % case)
            return
    for row in b:
        if '.' in row:
            print('Case #%d: Game has not completed' % case)
            return

    print('Case #%d: Draw' % case)


def solvet(f, case):
    board = []
    for i in range(4):
        board.append([x for x in f.readline()])
    solveb(board, case)
    f.readline()

def solve(fname):
    with open(fname, 'r') as f:
        numt = int(f.readline())
        for i in range(numt):
            solvet(f, i+1)

if __name__=='__main__':
    solve(sys.argv[1])
