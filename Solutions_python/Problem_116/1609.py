#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Description"""

__author__ = 'Pedro Larroy'
__version__ = '0.1'

import os
import sys
import copy


def read_input(fname):
    fd = open(fname, 'rb')
    ncases = 0
    boards = []
    board = [[None]*4]*4
    nline = 0
    for (i,line) in enumerate(fd.readlines()):
        line = line.rstrip()
        if i == 0:
            ncases = int(line)
        else:
            if nline < 4 and len(line):
                board[nline] = list(line)
                if nline == 3:
                    boards.append(copy.deepcopy(board))
                    nline = 0
                else:
                    nline += 1
            else:
                #assert(len(line) == 0)
                nline = 0
    return boards

class Game:

    X_WON = 'X won'
    O_WON = 'O won'
    DRAW = 'Draw'
    NOT_COMPLETED = 'Game has not completed'
    def __init__(self):
        self.reset()

    def reset(self):
        self.X = 0
        self.O = 0
        self.empty = 0
        self.result = Game.NOT_COMPLETED
        self.nstrides = 0

    def process(self, stride):
        if self.result == Game.NOT_COMPLETED:
            for c in stride:
                if c == 'X':
                    self.X += 1
                elif c == 'O':
                    self.O += 1
                elif c == 'T':
                    self.O += 1
                    self.X += 1
                elif c == '.':
                    self.empty += 1

            if self.X == 4:
                self.result = Game.X_WON
            if self.O == 4:
                self.result = Game.O_WON
            self.X = 0
            self.O = 0
        self.nstrides += 1
        if self.nstrides >= 4 and self.empty == 0:
            self.result = Game.DRAW
        return self.result

def solve(board):
    assert(len(board) == 4)
    assert(len(board[0]) == 4)
    g = Game()
    #hori
    for row in board:
        res = g.process(row)
        if res == Game.X_WON or res == Game.O_WON:
            return res

    #vertical
    for coli in range(0,4):
        stride = []
        for rowi in range(0,4):
            stride.append(board[rowi][coli])
        res = g.process(stride)
        if res == Game.X_WON or res == Game.O_WON:
            return res

    # diag
    diag1 = []
    diag2 = []
    for i in range(0,4):
        diag1.append(board[i][i])
        diag2.append(board[i][3-i])

    res = g.process(diag1)
    if res == Game.X_WON or res == Game.O_WON:
        return res

    res = g.process(diag2)
    return res

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    fname = sys.argv[1]
    boards = read_input(fname)
    for (i, board) in enumerate(boards):
        print 'Case #{0}: {1}'.format(i+1, solve(board))

    return 1

if __name__ == '__main__':
    sys.exit(main())

