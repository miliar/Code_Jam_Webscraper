# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
def maxRange(bathroom):
    ind=[i for i, x in enumerate(bathroom) if x == 1]
    rng=0
    l=0
    r=0
    for i in range(len(ind)-1):
        k=(ind[i+1]-ind[i])
        if rng<k:
            rng=k
            l=ind[i]
            r=ind[i+1]
    return (l,r,rng)

def updated(bathsroom):
    l,r,rng=maxRange(bathsroom)
    bathsroom[(l+r)//2]=1
    return (bathsroom,(l+r)//2)


for i in range(int(input())):
    n,m=map(int,input().split())
    bathroom=[1]+[0]*n+[1]
    for p in range(m):
        bathroom,t=updated(bathroom)
    temp = bathroom[:t]
    temp.reverse()
    ls = temp.index(1)
    temp = bathroom[t + 1:]
    rs = temp.index(1)
    print("Case #{0}: {1} {2}".format(i+1,max(ls,rs),min(ls,rs)))

