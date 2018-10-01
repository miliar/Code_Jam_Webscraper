# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 10:28:32 2017

@author: Ammi
"""

t = int(input())

def gen_number(n):
    a = []
    while n>0:
        a.append(n%10)
        n = n//10
    for i in range(1,len(a)):
        if a[i]>a[i-1]:
            a[i]=a[i]-1
            for j in range(0,i):
                a[j]=9
    for i in range(len(a)):
        n = n + a[i]*int(10**i)
    return n

for i in range(t):
    n = int(input())
    print("Case #" +str(i+1)+": "+ str(gen_number(n)))