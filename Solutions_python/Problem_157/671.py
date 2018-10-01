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
    L,X = gcj.tokens(2, int) #can be token(int) or tokens(N, int) # can be int or str
    S = gcj.token(str)
    
    dij = S*X
    
    #print('dij:', dij)    
    #print('B:', B)    
    #print('K:', K)    

    #SOLVE
    parity=1
    i=0
    # Get i
    while(i+1<len(dij)):
        if dij[i]=='i':
            i+=1
            break

        temp_ret = _solve(dij[i],dij[i+1])
 
        if temp_ret[1]==-1:
            parity*=-1

        if (len(dij)<=2+i):
            dij = temp_ret[0]
            break;
                    
        if temp_ret[0]=='0':
            dij=dij[2:]
            continue
        
        dij=temp_ret[0]+dij[2:]
        
    # Get j
    while(i+1<len(dij)):
        if dij[i]=='j':
            i+=1
            break

        temp_ret = _solve(dij[i],dij[i+1])
 
        if temp_ret[1]==-1:
            parity*=-1

        if (len(dij)<=2+i):
            dij = dij[:i]+temp_ret[0]
            break;
                    
        if temp_ret[0]=='0':
            dij=dij[:i]+dij[i+2:]
            continue
        
        dij=dij[:i]+temp_ret[0]+dij[i+2:]
       
    # Get k
    while(len(dij)>3):

        temp_ret = _solve(dij[i],dij[i+1])
 
        if temp_ret[1]==-1:
            parity*=-1

        if (len(dij)<=2+i):
            dij = dij[:i]+temp_ret[0]
            break;
                    
        if temp_ret[0]=='0':
            dij=dij[:i]+dij[i+2:]
            continue
        
        dij=dij[:i]+temp_ret[0]+dij[i+2:]

    # END
    
    if (dij=="ijk" and parity ==1):    
        return "YES"
        
    return "NO"

def _solve(a,b):
    if a==b:
        return ('0',-1)

    if a=='i' and b=='j':
        return ('k',1)
    if a=='i' and b=='k':
        return ('j',-1)

    if a=='j' and b=='i':
        return ('k',-1)
    if a=='j' and b=='k':
        return ('i',1)
    
    if a=='k' and b=='i':
        return ('j',1)
    if a=='k' and b=='j':
        return ('i',-1)
    
    
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
