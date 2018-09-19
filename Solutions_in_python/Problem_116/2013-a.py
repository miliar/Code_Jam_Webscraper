#!/usr/bin/env python

import pprint
import sys
from collections import Counter

def read_board(inp):
    board = {}
    for p in range(4):
        line = inp.next()
        for q in range(4):
            board[p,q] = line[q]
    inp.next()
    return board

def check_board(board):
    return check_horizontal(board) \
           or check_vertical(board) \
           or check_diagonal(board) \
           or check_completed(board)

def check_completed(board):
    if '.' in board.values():
        return "Game has not completed"
    else:
        return "Draw"

def check_horizontal(board):
    for q in range(4):
        line = [ board[p,q] for p in range(4) ]
        r = eval_line(line)
        if r:
            return r

def check_vertical(board):
    for p in range(4):
        line = [ board[p,q] for q in range(4) ]
        r = eval_line(line)
        if r:
            return r

def check_diagonal(board):
    line = [board[p,p] for p in range(4) ]
    r = eval_line(line)
    if r:
        return r
    line = [board[p, 3-p] for p in range(4) ]
    r = eval_line(line)
    if r:
        return r

def eval_line(line):
    counts = Counter(line)
    if counts['X'] == 4:
        return 'X won'
    elif counts['X'] == 3 and counts['T'] == 1:
        return 'X won'
    elif counts['O'] == 4:
        return 'O won'
    elif counts['O'] == 3 and counts['T'] == 1:
        return 'O won'

def main():
    inp = iter(sys.stdin)
    num_cases = int(inp.next())
    for case in range(1, 1 + num_cases):
        print "Case #%d: %s" %(case, check_board(read_board(inp)))

if __name__ == '__main__':
    main()
