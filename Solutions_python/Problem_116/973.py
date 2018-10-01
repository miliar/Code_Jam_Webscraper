#! /usr/bin/python

import sys

def mapt(row, p):
    mr = ""
    for c in row:
        if c == 'T':
            mr += p
        else:
            mr += c
    return mr

def checkdots(row):
    if row.find(".") != -1:
        return True
    else:
        return False

def checkforwinner(set, p):
    if mapt(set, p) == 4*p:
        return True
    else:
        return False

def checkforwinners(set):
    if checkforwinner(set, "X"):
        return "X"
    if checkforwinner(set, "O"):
        return "O"
    return False


def checkboardstatus(n, board):
    #print "Test case %d" % (n+1)
    #print board

    fullboard = True

    #Check rows
    for r in range(4):
        row = board[r]
        win = checkforwinners(row)
        if win:
            return win

        if checkdots(row):
            fullboard = False


    #Check columns
    for c in range(4):
        col = ""
        for r in range(4):
            col += board[r][c]

        win = checkforwinners(col)
        if win:
            return win

    #Check diagonals
    # -- TL to BR                
    diag = ""
    for d in range(4):
        diag += board[d][d]
    win = checkforwinners(diag)
    if win:
        return win


    # -- TR to BL                
    diag = ""
    for d in range(4):
        diag += board[d][3-d]
    win = checkforwinners(diag)
    if win:
        return win

    if fullboard:
        return ""
    else:
        return "."
    return

with sys.stdin as inp:
    numbertestcases = int(inp.readline())

    for n in range(numbertestcases):
        board = []
        for r in range(4):
            board.append(inp.readline()[:-1])

        inp.readline()
        stat = checkboardstatus(n, board)
        if stat=="X":
            print "Case #%d: X won" % (n+1)
        elif stat=="O":
            print "Case #%d: O won" % (n+1)
        elif stat==".":
            print "Case #%d: Game has not completed" % (n+1)
        else:
            print "Case #%d: Draw" % (n+1)

        

