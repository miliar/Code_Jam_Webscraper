#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dan
#
# Created:     07/05/2011
# Copyright:   (c) Dan 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

file1=r"d:\Download Firefox\B-large.in"
output=r"d:\Download Firefox\B-large.out"

def solve(c,combine,d,opposite,n,series,k):
    final=[]                # final solution
    lf=len(final)           # lenght of final
    for elem in series[0]:
        if lf==0:
            final.append(elem)
            lf=lf+1
        else:
            final.append(elem)
            lf=lf+1
            if lf>=2:
                for elem2 in combine:
                    if elem2[0]+elem2[1]==final[lf-2]+final[lf-1] or elem2[1]+elem2[0]==final[lf-2]+final[lf-1]:
                        final.pop(lf-1)
                        final.pop(lf-2)
                        lf=len(final)
                        final.append(elem2[2])
                        lf=lf+1
                        break

                #check for opposite
                for j in range(lf-2,-1,-1):
                    t=0
                    if t==0:
                        for elem2 in opposite:
                            if final[lf-1]+final[j]==elem2 or final[j]+final[lf-1]==elem2:
                                final=[]
                                lf=0
                                t=1
                                break
                        if t==1:
                            break
    text=str(final)
    text=text.replace('\'','')
    g.write('Case #%d: %s\n'% (k,text))



f=open(file1,'r')
g=open(output,'w')
aux=f.readline().rstrip('\n')
t=int(aux)
for i in range(1,t+1):
    line=f.readline().rstrip('\n')
    list=line.split()
    c=int(list[0])
    if c>0:
        combine=list[1:c+1]
    else:
        combine=[]
    d=int(list[c+1])
    if d>0:
        opposite=list[c+2:c+2+d]
    else:
        opposite=[]
    n=int(list[c+d+2])
    series=list[c+d+3:]
    solve(c,combine,d,opposite,n,series,i)


f.close()
g.close()


