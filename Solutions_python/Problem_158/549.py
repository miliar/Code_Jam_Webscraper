# encoding: UTF-8

from __future__ import absolute_import, division

import collections
import itertools
import sys

class gcj:
    IN = open('D:\code jam\input.in', 'r')
    OUT = open('D:\code jam\output.txt', 'w')
    buf = None

    identity = lambda x: x

    @classmethod
    def _read_line(cls):
        if cls.buf:
            res = cls.buf
            cls.buf = None
        else:
            res = cls.IN.readline()
        if not res:
            raise EOFError()
        return res

    @classmethod
    def line(cls, conv=identity):
        line = cls._read_line()
        return conv(line.rstrip(b'\r\n'))

    @classmethod
    def splitline(cls, conv=identity):
        line = cls._read_line()
        return [conv(x) for x in line.split()]

    @classmethod
    def whitespace(cls):
        line = None
        while not line:
            line = cls._read_line()
            i = 0
            l = len(line)
            while i < l and line[i].isspace():
                i += 1
            line = line[i:]
        cls.buf = line

    @classmethod
    def token(cls, conv=identity):
        cls.whitespace()
        line = cls._read_line()
        i = 0
        l = len(line)
        while i < l and not line[i].isspace():
            i += 1
        cls.buf = line[i:] if i < l else None
        return conv(line[:i])

    @classmethod
    def tokens(cls, cnt, conv=identity):
        #tokens=[]
        #for _ in range(cnt):
        #    tokens.append(cls.token(conv))
        #return tokens   
        return [cls.token(conv) for _ in range(cnt)]

    current_case = 0

    @classmethod
    def case(cls):
        cls.current_case += 1
        return 'Case #{}:'.format(cls.current_case)
    
    @classmethod
    def writefile(cls, case, solve):
        cls.OUT.write( case + " " + str(solve) + '\n')
        return
    

def solve():
    #Get Variables
    X,R,C = gcj.tokens(3, int) #can be token(int) or tokens(N, int) # can be int or str

    #print('A:', A)    
    #print('B:', B)    
    #print('K:', K)    

    #SOLVE
    L = min(R,C)
    H = max(R,C)
    
    if (X > H ):
        return "RICHARD"
    
    if ((R*C)%X!=0):
        return "RICHARD"
    
    if X >= 7 and L>3:
        return "RICHARD"

    #odd
    if X%2!=0:
        #side = (X+1)/2
        if L < (X+1)/2:
            return "RICHARD"
    #even
    if X%2==0:
        small_side=X/2
        large_side=small_side+1
        if L < small_side or H < large_side:
            return "RICHARD"
        
    if L==2:
        if X>2*(H-X)+3:
            return "RICHARD"
    
    return "GABRIEL"

def main():
    t = gcj.token(int)
    for _ in range(t):
        case = gcj.case()
        if case == "Case #8:":
            j=8
        result = solve()
        
        gcj.writefile(case, result)
        print(case, result)

main()
