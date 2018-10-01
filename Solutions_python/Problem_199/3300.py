#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 02:02:37 2017

@author: leello
"""
add = []
def gen(k, n):
    ini = '1' * k
    add = []
    for i in range(0, n-k+1):
        add.append(i*'0' + ini + (n - i - k)*'0')
    return add

def neighbours(s, add):
    neigh = []
    for e in add:
        res = []
        c = 0
        for i in range(len(s)):
            dig = (int(s[i]) + int(e[i])) % 2
            if dig == 1:
                c +=1
            res.append(str(dig))
        neigh.append((c, "".join(res)))
    neigh.sort()
    return [n[1] for n in neigh]


def dfs(s):
    pivot = s
    S = [pivot]
    P = {pivot: 0}
    
    while True:
        if int(pivot) == 0:
            return True, P[pivot]
        neigh = neighbours(pivot, add)
        for n in neigh:
            if n not in P:
                P[n]= P[pivot] + 1
            else:
                P[n] = min(P[n], P[pivot] + 1)
        minim = 500000
        prev = str(pivot)
        for k in P:
            if k not in S:
                if P[k] < minim:
                    pivot =k
                    minim = P[k]
        
        if prev==pivot:
            return False, 0
        S.append(pivot)
        
        


t = {'+': '0', '-': '1'}
T = int(input())
for i in range(T):
    S, K = raw_input().split(' ')
    k = int(K)
    s = "".join([t[x] for x in S])
    add = gen(k, len(s))
    res = dfs(s)
    if res[0]:
        print("Case #{0}: {1}".format(i+1, res[1]))
    else:
        print("Case #{0}: {1}".format(i+1, "IMPOSSIBLE"))

