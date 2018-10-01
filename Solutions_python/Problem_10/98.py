#!/usr/bin/env python
#coding=utf-8
"""
    Round 1C
"""

if __name__=='__main__':       

    fin=open('A-large.in','r')
    fout=open('A-large.out','w')
    
    line=fin.readline()
    N=int(line.strip()) # Case count
    for i in range(N):
        case_id=i+1
        line1=fin.readline().strip()
        [Ps,Ks,Ls]=line1.split()
        P=int(Ps)
        K=int(Ks)
        L=int(Ls)
        #print P,K,L
        line2=fin.readline().strip()
        Ls=line2.split()
        Lf=[]
        for j in range(L):
            Lf.append(int(Ls[j]))
        #print Lf
        
        Lf.sort()
        #print Lf
        
        totalPress=0
        pos=1
        l=L-1
        c=0
        while l>=0:
            
            totalPress+=Lf[l]*pos
            l-=1
            c+=1
            if c==K:
                c=0
                pos+=1
            
        print 'Case #'+str(case_id)+': '+str(totalPress)
        fout.write('Case #'+str(case_id)+': '+str(totalPress)+'\n')
    
    
    fin.close()
    fout.close()
