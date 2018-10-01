#!/usr/bin/env python
#
# Tic-Tac-Toe-Tomek
# Author: Jon Makela, Apr 2013
# Language: Python 2.7

# Bug: checkHoriz and checkVert names are swapped, vert = row.

# Small: 1 ≤ T ≤ 10
# Large: 1 ≤ T ≤ 1000

#from pprint import pprint

# 2 incorrects on small input for
# capitalizing Won in "X/O won" output...
# GG
#

import sys

FILE_LOC = "./sample.txt"
DBG = False

WILD = 'T'
X = 'X'
O = 'O'
EMPTY = '.'

DRAWN = 'D'
NOTDONE = 'N'

GOOD_X = set((WILD, X))
GOOD_O = set((WILD, O))
GOOD = set((WILD, X, O))

X_WON = "X won"
O_WON = "O won"
DRAW_STR = "Draw"
NOT_DONE_STR = "Game has not completed"

def readFile():
    with open(FILE_LOC) as fh:
        num_test = int(fh.readline())
        data = []
        for i in xrange(num_test):
            tmp = ""
            for j in xrange(4):
                tmp_ = fh.readline()
                while len(tmp_) <= 1:
                    tmp_ = fh.readline()
                tmp += tmp_
            data.append(readBoard(tmp))
    return data


def readBoard(data_entry):
    board = [['.']*4 for i in xrange(4) ]   # 4x4
    col = row = 0
    for ch in data_entry:
        if ch.isspace():
            continue
        else:
            board[row][col] = ch
            col += 1
            if (col % 4) == 0:
                row += 1
                col = 0
    #if DBG: pprint(board)
    return board

def printResult(result_type):
    "supports X, O, DRAWN, ELSE=notdone"
    if result_type == X:
        printCase(printResult.num, X_WON)
    elif result_type == O:
        printCase(printResult.num, O_WON)
    elif result_type == DRAWN:
        printCase(printResult.num, DRAW_STR)
    else:
        printCase(printResult.num, NOT_DONE_STR)
    printResult.num += 1
    return
printResult.num = 1

def printCase(num, str):
    print("Case #%d: %s" % (num,str))



def checkState(board):
    diag = checkDiag(board)
    if DBG: print "diag "+diag
    if diag is not EMPTY:
        return diag
    vert = checkVert(board)
    if DBG: print "vert "+vert
    if vert is not EMPTY:
        return vert
    horiz = checkHoriz(board)
    if DBG: print "horiz "+horiz
    if horiz is not EMPTY:
        return horiz

    if checkBoardFull(board):
        # draw
        return DRAWN
    else:
        return NOTDONE

def checkDiag(board):
    flag1 = board[0][0]
    bad1 = False

    flag2 = board[0][3]
    bad2 = False

    for i in xrange(1,4):
        flag1 = isMore(flag1, board[i][i])
        if flag1 is False:
            bad1 = True
        flag2 = isMore(flag2, board[i][3-i])
        if flag2 is False:
            bad2 = True
    if bad1 and bad2:
        return EMPTY
    elif flag1 is O or flag2 is O:
        return O
    elif flag1 is X or flag2 is X:
        return X

def checkVert(board):
    for i in xrange(0,4):
        old_item = board[0][i]
        for j in xrange(1,4):
            item = isMore(old_item, board[j][i])
            if item is False:
                old_item = False
                break
            old_item = item
        if old_item is not False:
            return old_item
    return EMPTY


def checkHoriz(board):
    for row in board:
        old_item = row[0]
        for i in xrange(1,4):
            item = isMore(old_item, row[i])
            if item is False:
                old_item = False
                break
            old_item = item
        if old_item is not False:
            return old_item
    return EMPTY

def checkBoardFull(board):
    for el in board:
        for idx in el:
            if idx == '.':
                return False
    return True

def isMore(old,new):
    "Returns False, X, or O depending on if args match"
    if old not in GOOD or new not in GOOD:
        return False
    elif old in GOOD_X and new in GOOD_X:
        return X
    elif old in GOOD_O and new in GOOD_O:
        return O
    else:
        return False


def main():
    if len(sys.argv) > 0:
        global FILE_LOC
        FILE_LOC = sys.argv[1]
    data = readFile()
    for board in data:
        state = checkState(board)
        printResult(state)


if __name__ == '__main__':
    main()