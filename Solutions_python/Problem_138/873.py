#!/usr/bin/env python
# -*- coding: utf-8 -*-
nx=int(input())
i=0
cheat=[]
nocheat=[]
while i<nx:
    input()
    naomi=sorted([float(x) for x in str(input()).strip().split(" ")])
    ken=sorted([float(x) for x in str(input()).strip().split(" ")])
    n=0
    k=0
    nwins=0
    kwins=0
    while (n<len(naomi) and k<len(ken)):
        while n+1<len(naomi) and naomi[n]<ken[k]:
            n+=1

        if naomi[n]>ken[k]:
            nwins+=1

        n+=1
        k+=1
    cheat.append(nwins)
    nwins=0
    n=len(naomi) -1
    kh=len(ken) -1
    kl=0
    while (n>=0 and k>=0):
        while (n>=0 and kl<len(ken) and naomi[n] > ken[kh]):
            n-=1
            kl+=1
            nwins+=1
        n-=1
        kh-=1
    nocheat.append(nwins)
    i+=1
for i in range(0,len(cheat)):
    print("Case #",i+1,": ",cheat[i]," ",nocheat[i],sep="")