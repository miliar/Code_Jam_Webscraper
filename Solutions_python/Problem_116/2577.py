#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ben
#
# Created:     12/04/2013
# Copyright:   (c) Ben 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import array, sys


def search(matrix):
    nf=0
    for rows in matrix:
        r1=''.join(map(str,rows))
        if r1.count("X")==4:
            return "X won"
        if r1.count("O")==4:
            return "O won"
        if r1.count("X")==3 and r1.count("T")==1:
            return "X won"
        if r1.count("O")==3 and r1.count("T")==1:
            return "O won"
        if r1.count(".")>=1:
            nf=1
    for rows in zip(*matrix):
        r2=''.join(map(str,rows))
        if r2.count("X")==4:
            return "X won"
        if r2.count("O")==4:
            return "O won"
        if r2.count("X")==3 and r2.count("T")==1:
            return "X won"
        if r2.count("O")==3 and r2.count("T")==1:
            return "O won"
        if r2.count(".")>=1:
            nf=1
    r3=[matrix[0][0],matrix[1][1],matrix[2][2],matrix[3][3]]
    if r3.count("X")==4:
        return "X won"
    if r3.count("O")==4:
        return "O won"
    if r3.count("X")==3 and r3.count("T")==1:
        return "X won"
    if r3.count("O")==3 and r3.count("T")==1:
        return "O won"
    if r3.count(".")>=1:
        nf=1
    r4=[matrix[3][0],matrix[2][1],matrix[1][2],matrix[0][3]]
    if r4.count("X")==4:
        return "X won"
    if r4.count("O")==4:
        return "O won"
    if r4.count("X")==3 and r4.count("T")==1:
        return "X won"
    if r4.count("O")==3 and r4.count("T")==1:
        return "O won"
    if r4.count(".")>=1:
        nf=1
    if nf==1:
        return "Game has not completed"
    return "Draw"


def main():
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)
    t = int(f.readline())
    s=[[]]*4
    for _t in range(t):
        for i in range(4):
            s[i] = list(f.readline().strip())
        print("Case #" + str(_t+1) + ": " + search(s))
        f.readline()

##Case #1: X won
##Case #2: Draw
##Case #3: Game has not completed
##Case #4: O won
##Case #5: O won
##Case #6: O won


if __name__ == '__main__':
    main()
