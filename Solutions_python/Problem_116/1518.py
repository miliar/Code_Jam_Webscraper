import numpy as np
import os
import re

def is_full(board):
    for i in range(len(board[:,0])):
        for j in range(len(board[0,:])):
            if (board[i,j] != 'X' and board[i,j] != 'O' and board[i,j] != 'T'):
                return 0
    return 1

def is_win(array):
    nx = 0
    no = 0
    for i in range(len(array)):
        if (array[i] == 'O' or array[i] == 'T'):
            no += 1
        if (array[i] == 'X' or array[i] == 'T'):
            nx += 1
    if (no == 4):
        return 1
    elif (nx == 4):
        return -1
    return 0

def solve(board):
    for i in range(len(board[:,0])):
        col = is_win(board[:,i])
        row = is_win(board[i,:])
        if (col != 0 or row != 0):
            if (col == 1 or row == 1):
                return "O won"
            else :
                return "X won"
        diag1 = is_win(np.array([board[0,0], board[1,1], board[2,2], board[3,3]]))
        diag2 = is_win(np.array([board[0,3], board[1,2], board[2,1], board[3,0]]))
        if (diag1 != 0 or diag2 != 0):
            if (diag1 == 1 or diag2 == 1):
                return "O won"
            else :
                return "X won"
    return "None"

def main():
    infile = "Alarge.in"
    inf = open(infile, 'r')

    outfile = "p1.dat"
    outf = open(outfile, 'w')

    lnum = 1
    case = 0
    for line in inf:
        if (lnum == 1):
            ncases = int(line.split()[0])
        if ((lnum - 1) % 5 == 0):
            if (case > 0):
                message = solve(board)
                if (message == "None"):
                    if (is_full(board)):
                        message = "Draw"
                    else:
                        message = "Game has not completed"
                outf.write("Case #" + str(case) + ": " + message + "\n")
            case += 1
            board = np.zeros( (4,4) , dtype='S')
            row = 0
        else:
            lstring = str(line).rstrip()
            for i in range(len(lstring)):
                board[i,row] = lstring[i]
            row += 1
        lnum += 1
        
if __name__ == '__main__':
     main()
