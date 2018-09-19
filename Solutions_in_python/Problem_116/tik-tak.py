#!/bin/python

import sys

allowed = ['X','O','T','.']
xwin = ['X', 'T']
owin = ['O', 'T']
xwin1 = ['X']
owin1 = ['O']

def check(i,j,m):
    stat = False
    cc, cc1 = [], []
    ret =""
    curr = m[i][j]
    if curr == 'X':
        cc, cc1 = set(xwin), set(xwin1)
    elif (curr == 'O'):
        cc, cc1 = set(owin), set(owin1)
    row = set(m[i])
    col = set([m[0][j],m[1][j],m[2][j],m[3][j]])
    #print m[i], m[:][j]
    diag1 = set([m[0][0],m[1][1],m[2][2],m[3][3]])
    diag2 = set([m[0][3],m[1][2],m[2][1],m[3][0]])
    if ((cc == row) or (cc == col) or (cc == diag1) or (cc == diag2)):
        stat = True
        ret = '%s won' %(curr)
    if ((cc1 == row) or (cc1 == col) or (cc1 == diag1) or (cc1 == diag2)):
        stat = True
        ret = '%s won' %(curr)
    return stat, ret
    


def checkWin(m):
    done = True
    for i, row in enumerate(m):
        for j, col in enumerate(row):
            if m[i][j] not in allowed:
                return -1, "Error"
            if m[i][j] == '.':
                done = False
            status, txt = check(i,j,m)
            if status:
                return 2, txt
    if done:
        return 1, "Draw"
    else:
        return 0, "Game has not completed"
        
        
def output(num, matrix, ff):
    code, textt = checkWin(matrix)
    if code == -1:
        print "Case #",num,": Error"
    else:
        out="Case #%s: %s\n"%(num,textt)
        ff.write(out)
    
        

        
if __name__ == '__main__':
    ff = open("A-large.in")
    oo = open('output.txt', 'w')
    total = long(0)
    pos = long(0)
    buf = 0
    m = []
    l1 = long(1)
    for line in ff:
        if pos == 0:
            total = long(line)
        else:
            l = line.strip()
            if buf == 4:
                output(l1,m, oo)
                buf = 0
                m = []
                l1 += 1
            else:
                m.extend([l])
                buf +=1
        pos += 1
        
    ff.close()
    oo.close()
        
    #m0 =["XXXT","....","OO..","...."]
    #m  = ["XOXT", "XXOO", "OXOX", "XXOO"]
    #m1 = ["XOX.", "OX..","....", "...."]
    #m2 = ["OOXX", "OXXX", "OX.T","O..O"]
    #m3 = ["XXXO", "..O.", ".O..", "T..."]
    #m4 = ["OXXX", "XO..", "..O.", "...O"]
    
    #output(1,m0)
    #output(2,m)
    #output(3,m1)
    #output(4,m2)
    #output(5,m3)
    #output(6,m4)