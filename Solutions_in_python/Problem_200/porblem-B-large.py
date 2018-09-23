#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 19:37:58 2017

@author: xijiaqi1997
"""

def tidy(n):
    for i in reversed(range(n+1)):
        si = str(i)
        flag = True
        for j in range(len(si)-1):
            if si[j] > si[j+1]:
                flag = False
        if flag == True:
            return i
        
def tidy_large(n):
    ns = str(n)
    if ns[-1] != 0:
        for i in range(len(ns)-1):
            if int(ns[i]) > int(ns[i+1]):
                ns = ns[:i]+str(int(ns[i])-1)+'9'*len(ns[i+1:])
                break
    else:
        ns = str(n-1)
    flag = True
    for i in range(len(ns)-1):
        if int(ns[i]) > int(ns[i+1]):
            flag = False
    if flag:
        return int(ns)
    else:
        return tidy_large(int(ns))
            
def main():
    cases = open('B-large.in.txt','r').readlines()
    cases = [int(cases[i].rstrip('\n')) for i in range(len(cases))]
    result = open('result-b-large.txt','w')
    for i in range(1,len(cases)):
        result.write('Case #%s: %s\n' % (i, tidy_large(cases[i])))
    result.close()

main()