#!/usr/bin/env python

SIZE = 4

def run_one(board):
    for mark in ('X', 'O'):
        # Rows and Columns
        for i in range(SIZE):
            if all(board[i][x] in (mark, 'T') for x in range(SIZE)) or \
               all(board[x][i] in (mark, 'T') for x in range(SIZE)):
                return '{0} won'.format(mark)

        # Diagonals
        if all(board[x][x] in (mark, 'T') for x in range(SIZE)) or \
           all(board[3-x][x] in (mark, 'T') for x in range(SIZE)):
            return '{0} won'.format(mark)

    # Not finished
    for i in range(SIZE):
        if '.' in board[i]:
            return 'Game has not completed'

    # Draw
    return 'Draw'


def run(lines):
    output = []

    # Number of test cases
    T = int(lines.popleft())
    for t in range(T):
        # Game board
        board = [list(lines.popleft().rstrip('\r\n')) for row in range(SIZE)]

        result = run_one(board)

        output.append('Case #{0}: {1}'.format(t + 1, result))

        # Empty line between boards
        lines.popleft()

    return output


# Google Code Jam submissions must run stand-alone.
# This code shall be copied into each solution.
if __name__ == '__main__':
    import os
    import sys
    from collections import deque

    infile = sys.argv[1]
    with open(infile) as file:
        lines = deque(file.readlines())
        output = run(lines)
        print os.linesep.join(output)
