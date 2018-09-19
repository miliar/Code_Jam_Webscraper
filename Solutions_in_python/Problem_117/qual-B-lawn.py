#!/usr/bin/python
import sys

T = int(sys.stdin.readline())
for test_case in xrange(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    board = [map(int, sys.stdin.readline().split())[:M]
             for row in xrange(N)]
    row_high = [max(row) for row in board]
    col_high = [max(col) for col in zip(*board)]
    answer = "YES"
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell < row_high[r] and cell < col_high[c]:
                answer = "NO"
    print "Case #{0}: {1}".format(test_case, answer)

        
        
