# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:17:00 2017

@author: amitrecords
"""
#GOOGLE CODE JAM
def flip(c):
    n=str()
    for i in range(len(c)):
        if c[i]=='-':
            n=n + '+'
        else:
            n=n + '-'
    return n
def solution(S,K):
    i=0
    num=0
    N=len(S)
    idl=''
    for j in range(N): idl=idl+ '+' 
    while S != idl:
        if S[i] == '-':
            if i+K-1<len(S):
                tmp=flip(S[i:i+K])
                S=S[:i]+tmp+S[i+K:]
                #print('flip returned',S)
                num+=1
            else:
                num='IMPOSSIBLE'
                return num
        i=i+1
        #print(S,i)
    return num
ip=open('input.txt') 
T=int(ip.readline().strip())
op=open('output.txt','w') 
for i in range(T):
    [S,K]=ip.readline().strip().split()
    numflips=solution(S,int(K))
    op.write('Case #'+ str(i+1) + ': '+str(numflips)+'\n') 
op.close()