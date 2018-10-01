# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:54:02 2017

@author: Julien
"""

import os 

#for i in range(K):
#    m=max(N)
#    j=N.index(m)
#    
#    if m%2==1:
#        N[j]=(m-1)/2
#        N.insert(j+1,(m-1)/2)
#    else:
#        N[j]=(m)/2-1
#        N.insert(j+1,(m)/2)
#    
##    print(N)
#    
#print(N[j])
#print(N[j+1])

def solve2(N,K):
    N=[N]
    for i in range(K):
        m=max(N)
        j=N.index(m)
        
        if m%2==1:
            N[j]=(m-1)/2
            N.insert(j+1,(m-1)/2)
        else:
            N[j]=(m)/2-1
            N.insert(j+1,(m)/2)
        
    #    print(N)
    
    return [N[j+1],N[j]]






#while K>pow(2,I):
#    newN=[]
#    for i in N:
#        if i%2==1:
#            newN.append(int(i/2))
#        else:
#            newN.append(int(i/2)-1)
#        
#        newN.append(int(i/2))
#    N=newN
#    K-=pow(2,I)
#    I+=1

#S=sorted(list(set(N)),reverse=True)
#SOcc=[N.count(x) for x in S]
#
#if K<=SOcc[0]:
#    r=S[0]
#else:
#    r=S[1]
#
#newN=[]
#if r%2==1:
#    newN.append(int(r/2))
#else:
#    newN.append(int(r/2)-1)
#newN.append(int(r/2))
#
#print(newN)

N=[12032]
K=3534

def solve(N,K):

    dico={N:1}
    I=0
    
    while K>pow(2,I):
        dicoNew=dict()
        
        for i in dico:
            if i%2==1:
                try: dicoNew[(int(i/2))]+=dico[i]
                except: dicoNew[(int(i/2))]=dico[i]
            else:
                try: dicoNew[(int(i/2)-1)]+=dico[i]
                except: dicoNew[(int(i/2)-1)]=dico[i]
    
            try: dicoNew[(int(i/2))]+=dico[i]
            except: dicoNew[(int(i/2))]=dico[i]
        dico=dict(dicoNew)
    #    print(dico)
        K-=pow(2,I)
        I+=1
    #print(I)
    #print('PROUT')
    #print(K)
    res=[]
    for i in sorted(dico,reverse=True):
        
        if K<=dico[i]:
    #        print(i)
            if i%2==1:
                res.append(int(i/2))
            else:
                res.append(int(i/2)-1)
            res.insert(0,int(i/2))
            break
        K-=dico[i]
    return(res)





fh="C-small-2-attempt0.in"
chem="C:\CodeJam\ExoC"
fhOut='Solution_'+fh

with open(os.path.join(chem,fh),'r') as f:
    with open(os.path.join(chem,fhOut),'w') as fOut:
        CASE=int(f.readline())
        
        for c in range(CASE):
            l=(f.readline())
            [N,K]=[int(x) for x in l.split()]
            res=solve(N,K)
#            print(s +str(k))
#            print(res)
            fOut.write("Case #" +str(c+1) + ': ' + ' '.join([str(x) for x in res])+'\n')
            

#with open(os.path.join(chem,fh),'r') as f:
#    with open(os.path.join(chem,'2'+fhOut),'w') as fOut:
#        CASE=int(f.readline())
#        
#        for c in range(CASE):
#            l=(f.readline())
#            [N,K]=[int(x) for x in l.split()]
#            res=solve2(N,K)
##            print(s +str(k))
##            print(res)
#            fOut.write("Case #" +str(c+1) + ': ' + ' '.join([str(int(x)) for x in res])+'\n')

