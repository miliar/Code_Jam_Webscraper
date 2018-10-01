# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 19:32:15 2017

@author: cling
"""

def checkstate(state,s):
    if (state==0) and (s=='-'):
        return True
    if (state==1) and (s=='+'):
        return True
    return False

def flip(state):
    return 1-state
    
def solve(S,K):
    cnt = 0
    state = 0
    L = len(S)
    flipend = [0]*L
    for i in range(0,L-K+1):
        if checkstate(state,S[i]):
            state = flip(state)
            cnt += 1
            flipend[i+K-1] = 1
        if flipend[i]==1:
            state = flip(state)
    for i in range(L-K+1,L):
        if checkstate(state,S[i]):
            return -1
        if flipend[i]==1:
            state = flip(state)
    return cnt            

def main():
    with open('A-large.in','r') as f:
        line = f.readline()
        print line,
        i = 1
        for line in f:
            st = line.split(' ')
            cnt = solve(st[0],int(st[1]))
            if cnt==-1:
                output = 'IMPOSSIBLE'
            else:
                output = str(cnt)
            print 'Case #%d: %s' % (i,output)
            i += 1

if __name__ == '__main__':
    main()
