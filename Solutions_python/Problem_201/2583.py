#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:24:24 2017

@author: xijiaqi1997
"""

def bathstall(stall,n,memo = {}):
    try:
        return memo[(n,tuple(stall))]
    except:
        flag = True
        for i in range(1,len(stall)-1):
            if stall[i] == 0:
                if stall[i-1] == 0 or stall[i+1] == 0:
                    flag = False
        if n > 0 and flag:
            return (0,0)
        elif n > 0:
            mindis = {}
            for i in range(len(stall)):
                if stall[i] == 0:
                    left1 = i - (len(stall) - 1 - stall[::-1].index(1,len(stall)-1-i)) - 1 
                    right1 = stall.index(1,i) - i - 1
                    try:
                        mindis[min(left1,right1)].append((i,max(left1,right1)))
                    except:
                        mindis[min(left1,right1)] = [(i,max(left1,right1))]
            temp = sorted(mindis[sorted(mindis.keys(),reverse = True)[0]],key=lambda d: d[1], reverse = True)
            if len(temp) > 1:
                if temp[0][1] != temp[1][1]:
                    occupy = temp[0][0]
                else:
                    end = 0
                    for j in range(len(temp)):
                        if temp[j][1] != temp[0][1]:
                            end = j
                            break
                    if end == 0:
                        end = len(temp)
                    occupy = min(temp[0:end])[0]
            else:
                occupy = temp[0][0]
            newstall = stall[:]
            newstall[occupy] = 1
            memo[(n,tuple(stall))] = (temp[0][1],sorted(mindis.keys(),reverse = True)[0])
            if n > 1:
                return bathstall(newstall,n-1,memo)
            else:
                return (temp[0][1],sorted(mindis.keys(),reverse = True)[0])



            
def main():
    cases = open('C-small-1-attempt3.in.txt','r').readlines()
    cases = [line.rstrip('\n') for line in cases]
    result = open('result-c-small.txt','w')
    for i in range(1,len(cases)):
        n = int(cases[i].split(' ')[1])
        stall = [1]+[0]*int(cases[i].split(' ')[0])+[1]
        maxdis, mindis = bathstall(stall,n)
        result.write('Case #%s: %s %s\n' % (i, maxdis, mindis))
    result.close()
        
main()
                

    