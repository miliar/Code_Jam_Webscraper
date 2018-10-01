#!/usr/bin/python

import os, sys

def getSolution(game):

    for i in range(0,4):
        if game[i] == 'XXXX' or game[i] == 'XXXT' or game[i] == 'TXXX' or game[i] == 'XTXX' or game[i] == 'XXTX':
            print 'X won'
            return
        elif game[i] == 'OOOO' or game[i] == 'OOOT' or game[i] == 'TOOO' or game[i] == 'OTOO' or game[i] == 'OOTO':
            print 'O won'
            return
        
        dig1 = game[0][i] + game[1][i] + game [2][i] + game[3][i]
        if dig1 == 'XXXX' or dig1 == 'XXXT' or dig1 == 'TXXX' or dig1 == 'XTXX' or dig1 == 'XXTX':
            print 'X won'
            return
        elif dig1 == 'OOOO' or dig1 == 'OOOT' or dig1 == 'TOOO' or dig1 == 'OTOO' or dig1 == 'OOTO':
            print 'O won'
            return
    
    # check diagonal
    dig1 = game[0][0] + game[1][1] + game [2][2] + game [3][3]
    dig2 = game[0][3] + game[1][2] + game [2][1] + game [3][0]
    if dig1 == 'XXXX' or dig1 == 'XXXT' or dig1 == 'TXXX' or dig1 == 'XTXX' or dig1 == 'XXTX':
        print 'X won'
        return
    elif dig2 == 'XXXX' or dig2 == 'XXXT' or dig2 == 'TXXX' or dig2 == 'XTXX' or dig2 == 'XXTX':
        print 'X won'
        return
        
    if dig1 == 'OOOO' or dig1 == 'OOOT' or dig1 == 'TOOO' or dig1 == 'OTOO' or dig1 == 'OOTO':
        print 'O won'
        return
    elif dig2 == 'OOOO' or dig2 == 'OOOT' or dig2 == 'TOOO' or dig2 == 'OTOO' or dig2 == 'OOTO':
        print 'O won'
        return
        
    whole = game[0]+game[1]+game[2]+game[3]
    if whole.find('.') == -1:
        print 'Draw'
        return 
 
    print 'Game has not completed'
    return    

def solveEachSet(l, lineCnt):
    game = [l[lineCnt]]
    game[0] = game[0][0:4]
    lineCnt += 1
    game.append(l[lineCnt])
    game[1] = game[1][0:4]
    lineCnt += 1
    game.append(l[lineCnt])
    game[2] = game[2][0:4]
    lineCnt += 1
    game.append(l[lineCnt])
    game[3] = game[3][0:4]
    lineCnt += 1
    getSolution(game)
    return lineCnt+1

def main():
    s = sys.stdin.readlines()
    lineCnt = 0
    testCaseNum = int(s[lineCnt])
    lineCnt+=1
    for i in range(1, testCaseNum+1):
        print 'Case #'+str(i)+':',
        lineCnt = solveEachSet(s, lineCnt)

if __name__=="__main__":
    main()
