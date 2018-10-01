import numpy as np
import sys
import itertools

f=open('A-large.in', 'r')
f2=open('1_output.ou', 'w')

init=0
case=1
aliii=int(f.readline())


while case <= aliii:
    
    b=f.readline().replace('\n','').split(' ')

    D=int(b[0])
    N=int(b[1])
    S=[]
    K=[]
    
    for aux in xrange(N):
        b=f.readline().replace('\n','').split(' ')
        K.append(float(b[0]))
        S.append(float(b[1]))
    
    
    t_prev=0
    for i in range(len(S)-1,-1,-1):
        t=max((D-K[i])/S[i],t_prev)
        t_prev=t
    
        
    res=D/t
    
    
    
    print 'Case #'+str(case)+": "+str(res)
    f2.write('Case #'+str(case)+": "+str(res)+'\n')
    case+=1