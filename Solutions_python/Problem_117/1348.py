import numpy as np
import os
import re

def is_possible(board):
    #print board
    if (board.size == 1):
        return 1
    minval = np.amin(board)
    maxval = np.amax(board)
    mylist = np.unique(board)
    if (minval == maxval):
        return 1
    for w in range(len(mylist)):
        for i in range(len(board[:,0])):
            for j in range(len(board[0,:])):
                if (board[i,j] == mylist[w]):
                    rowsum = 0
                    colsum = 0
                    for k in range(len(board[i,:])):
                        if (board[i,k] <= mylist[w]):
                            colsum += 1
                    for k in range(len(board[:,j])):
                        if (board[k,j] <= mylist[w]):
                            rowsum += 1
                        
                    if (colsum != len(board[i,:]) and rowsum != len(board[:,j])):
                        return 0
                    
    return 1

def main():
    infile = "Blarge.in"
    inf = open(infile, 'r')

    outfile = "large.dat"
    outf = open(outfile, 'w')

    lnum = 1
    case = 0
    readrow = 0
    row = 0
    rowmax = 0
    for line in inf:
        if (readrow == 1 and row < rowmax):
            lstring = line.split()
            for i in range(len(lstring)):
                board[row,i] = int(lstring[i])
            row += 1
        if (readrow == 0 and lnum != 1):
            board = np.zeros( (int(line.split()[0]), int(line.split()[1])) )
            rowmax = int(line.split()[0])
            row = 0
            readrow = 1
        if (row == rowmax and row != 0):
            case += 1
            val = is_possible(board)
            if (val == 0):
                message = "NO"
            else :
                message = "YES"
            outf.write("Case #" + str(case) + ": " + message + "\n")
            readrow = 0
        lnum += 1
            


if __name__ == '__main__':
     main()
