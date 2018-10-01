# -*- coding: utf-8 -*-
import math as mt
import networkx as nx
"""
Created on Sat Apr 22 22:48:20 2017

@author: DELL GAMING
"""

t = int(input())
for i in range(1, t + 1):
    n, m = [int(x) for x in input().split(" ")]
    list = []
    time = []
    for j in range(m):
        list.append([int(x) for x in input().split(" ")])
    for k in range(m):
        time.append((n-list[k][0])/list[k][1])
    use = max(time)
    print('Case #{}: {}'.format(i,n/use))