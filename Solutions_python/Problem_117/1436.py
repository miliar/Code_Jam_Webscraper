#!/usr/bin/env python

def shaveRow(board, r, level):
    if len(filter(lambda x: x>level, board[r])):
        return
    for j in range(len(board[r])):
        if board[r][j]==level:
            board[r][j]=-level

def shaveCol(board, c, level):
    for i in range(len(board)):
        if board[i][c] > level:
            return
    for i in range(len(board)):
        if board[i][c] == level:
            board[i][c] = -level

def solve(board):
    rg = (min(map(min, board)), max(map(max, board)))
    for level in range(rg[0], rg[1]+1):
        for i in range(len(board)):
            shaveRow(board, i, level)
        for j in range(len(board[0])):
            shaveCol(board, j, level)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == level:
                    return "NO"
                    
    return "YES"

if __name__ == '__main__':
    z = raw_input()
    for i in range(1, int(z)+1):
        N, M = map(int, raw_input().split())
        board = []
        for n in range(N):
            board.append(map(int, raw_input().split()))

        print 'Case #%d: %s' % (i, solve(board))
    pass

