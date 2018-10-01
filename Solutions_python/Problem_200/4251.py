# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 19:21:02 2017

@author: Haseeb Bhai
"""
def is_tidy(j):
    l = list(str(j))
    if len(l) == 1:
        return True
    else:
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True

t = int(input())
for i in range(1, t + 1):
    n = int(input())    

    last_tidy = 1
    for j in range(1, n + 1):
        if is_tidy(j):
            last_tidy = j
    print("Case #{}: {}".format(i, last_tidy))