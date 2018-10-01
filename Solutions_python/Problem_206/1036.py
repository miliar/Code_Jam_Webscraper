#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 23:06:26 2017

@author: xijiaqi1997
"""
def horse(destination, N, KSdic):
    time = []
    for key in KSdic.keys():
        temp = (destination - key)/KSdic[key]
        time.append(temp)
    ter = max(time)
    return destination/ter
    
def main():
    cases = open('A-large.in-2.txt','r').readlines()
    cases = [line.rstrip('\n') for line in cases]
    result = open('RB-A-large.txt','w')
    count = 0
    i = 1
    while i < len(cases) - 1:
        destination, N = int(cases[i].split(' ')[0]),int(cases[i].split(' ')[1])
        KSdic= {}
        for j in range(i+1,i+N+1):
            KSdic[int(cases[j].split(' ')[0])] = int(cases[j].split(' ')[1])
        count += 1
        result.write('Case #%s: %s\n' % (count,horse(destination,N,KSdic)))
        i += N + 1
    result.close()
    
main()