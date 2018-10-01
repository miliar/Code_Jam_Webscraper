#!/usr/bin/env python

import re
import sys

def linewinner(line):
    if re.match("[XT][XT][XT][XT]",line):
        return "X"
    elif re.match("[OT][OT][OT][OT]",line):
        return "O"
    else:
        return "N"

t = int(sys.stdin.readline())
for case in range(1,t+1):
    board = []
    for i in range(0,4):
        board.append(sys.stdin.readline())
    sys.stdin.readline()
    boardbycolumns = map(lambda a: ''.join(map(lambda b: board[b][a], range(0,4))), range(0,4))
    diag1 = map(lambda a: board[a][a],range(0,4))
    diag1 = ''.join(diag1)
    diag2 = map(lambda a: board[a][3-a],range(0,4))
    diag2 = ''.join(diag2)
    linestocheck = board + boardbycolumns + [diag1,diag2]
    nowinner = True
    for line in linestocheck:
        if linewinner(line) == "X":
            print "Case #" + str(case) + ": X won"
            nowinner = False
            break
        elif linewinner(line) == "O":
            print "Case #" + str(case) + ": O won"
            nowinner = False
            break
    if nowinner:
        if re.search('\.',''.join(board)):
            print "Case #" + str(case) + ": Game has not completed"
        else:
            print "Case #" + str(case) + ": Draw"
