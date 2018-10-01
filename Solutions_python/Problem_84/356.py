#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

class OK(Exception):
    def __init__(self, ans):
        self.answer = ans
        
class NG(Exception): pass

Blue  = '#'
While = '.'

def isSq(pic, r, c):
    return pic[r][c]   == Blue and \
           pic[r][c+1] == Blue and \
           pic[r+1][c] == Blue and \
           pic[r+1][c+1] == Blue

def isOK(pic):
    for r in pic:
        for c in r:
            if c == Blue: return False

    return True
           
def search(pic, R, C):
    # 置き換えた場所を記憶しておいて、データ構造を直接変更して
    # 再帰呼び出しする
    # もしOKだったら、OK例外を出して、例外オブジェクトに答えを入れる

    ignore = set()

    if isOK(pic): raise OK(pic)

    # まずBlueを探す
    for r in range(R-1):
        for c in range(C-1):

            # 不可能な形は発見したらignoreに追加しておく
            if (r,c) in ignore: continue

            if isSq(pic, r, c):
                changed = (r,c)
                pic[r][c]    = '/'
                pic[r][c+1]  = '\\'
                pic[r+1][c]  = '\\'
                pic[r+1][c+1] = '/'

                search(pic, R, C)

                pic[r][c]     = Blue
                pic[r][c+1]   = Blue
                pic[r+1][c]   = Blue
                pic[r+1][c+1] = Blue
                
                

def testCase(cin):
    R,C = [int(n) for n in cin.readline().split()]
    #print R,C

    pic = []
    blueCnt = 0

    for r in range(R):
        ln = list(cin.readline().strip())
        blueCnt += ln.count(Blue)
        pic.append( ln )

    if blueCnt % 4 != 0:
        return "Impossible"

    try:
        search(pic, R,C)
    except OK, ok:
        return "\n".join( [ ''.join(row) for row in ok.answer ] )

    return "Impossible"
    
def main():
    stdin = sys.stdin
    T = int( stdin.readline() )

    for t in range(T):
        print "Case #%d:" % (t+1)
        print testCase(stdin)

if __name__ == '__main__':
    main()
