# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
from itertools import combinations
from itertools import permutations
def flip(array,l,r):
    a=array[:]
    for i in range(l,r):
        if a[i]=="+":a[i]="-"
        else:a[i]="+"
    return a



def solve(str,k):
    s=list(str)
    flag=False
    for t in range(len(s)+1):
        combo=combinations(range(len(s)-k+1),t)
        while True:
            try:
                a=combo.__next__()
                per=permutations(a)
                while True:
                    try:
                        ls=per.__next__()
                        arr = s[:]
                        for i in ls:
                            arr=flip(arr,i,i+k)
                        if set(arr) == {"+"}:
                            flag = True
                            break
                    except StopIteration:
                        if set(arr) == {"+"}:
                            flag = True
                        break
                    if flag:break

            except StopIteration:
                if set(arr)=={"+"}:
                    flag=True
                break
        if flag:break
    if flag:ans=(t)
    else:ans=("IMPOSSIBLE")
    return ans

for i in range(int(input())):
    s,r=tuple(input().split())
    print("Case #{0}: {1}".format(i+1,solve(s,int(r))))
