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
    N,K = gcj.tokens(2,int) #can be token(int) or tokens(N, int) # can be int or str

        
    print('N:', N)
    print('K:', K)
    #print('len_S:', len(N)) 

    l = [0,N+1]
    
    i=0
    while i<K:
        j=1
        maxi=0
        index_maxi=0
        while j<len(l):
            if l[j]-l[j-1] > maxi:
                maxi = l[j]-l[j-1]
                index_maxi=j
            j+=1
        #adicionar nova posição
        l = l[:index_maxi] + [ l[index_maxi-1] + maxi//2] + l[index_maxi:]
        
        i+=1 
    
    print('l:', l)
    result = str(l[index_maxi+1]-l[index_maxi]-1) + " " + str(maxi//2 - 1)
    #print('B:', B)    
    #print('K:', K)    

        
    return result


def main():
    t = gcj.token(int)
    for _ in range(t):
        case = gcj.case()
        if case == "Case #34:":
            j=1
        result = solve()
        
        gcj.writefile(case, result)
        print(case, result)

main()
