# -*- coding: utf-8 -*-
"""
Created on Sat May 03 19:35:27 2014

@author: eidanch
"""


def get_line():
    return raw_input().strip()

formatIntegerList = lambda s: list(map(int,s.split(' ')))

def standard_input():
    T = int(get_line())
    for i in range(T):
        A,B,K = tuple(formatIntegerList(get_line()))
        yield (i+1,(A,B,K))

def binlen(n):
    return len(str(bin(n)))-2

def cutbin(n):
    if n == 0:
        return 0
    return n - pow(2,binlen(n) - 1)

def calc(A,B,K):
    result = 0
    for a in range(A):
        for b in range(B):
            if a & b < K:
                result += 1
    return result

def handle_case(case):
    A,B,K = case
    return str(calc(A,B,K))
    
        
def main():
    for i,case in standard_input():
        print "Case #%d: %s" %(i,handle_case(case))        

if __name__ == '__main__':
    main()
    