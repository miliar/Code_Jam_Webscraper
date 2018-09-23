#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 22:36:35 2017

@author: xijiaqi1997
"""
def cake(mat):
    ca = mat
    for j in range(len(mat[0])):
        if all(mat[i][j] == '?' for i in range(len(mat))):
            pass
        elif all(mat[i][j] != '?' for i in range(len(mat))):
            pass
        else:
            have = []
            for i in range(len(mat)):
                if ca[i][j] != '?':
                    have.append(i)
            for h in range(len(have)):
                if h == 0:
                    for i in range(have[h]):
                        ca[i][j] = ca[have[h]][j]
                else:
                    for i in range(have[h-1]+1,have[h]):
                        ca[i][j] = ca[have[h]][j]
            for i in range(have[len(have)-1]+1,len(mat)):
                ca[i][j] = ca[have[len(have)-1]][j]
    for j in range(len(mat[0])):
        if all(mat[i][j] == '?' for i in range(len(mat))):
            if j == 0:
                for i in range(len(mat)):
                    ca[i][j] = ca[i][j+1]
            else:
                for i in range(len(mat)):
                    ca[i][j] = ca[i][j-1]
    for j in reversed(range(len(mat[0]))):
        if all(mat[i][j] == '?' for i in range(len(mat))):
            if j == len(mat[0])-1:
                for i in range(len(mat)):
                    ca[i][j] = ca[i][j-1]
            else:
                for i in range(len(mat)):
                    ca[i][j] = ca[i][j+1]
    return ca
                    
            
                    
                    

def main():
    cases = open('A-large.in.txt','r').readlines()
    cases = [line.rstrip('\n') for line in cases]
    result = open('result-R1A-A-large.txt','w')
    i = 1
    count = 0
    while i <= len(cases)-1:
        R,C = int(cases[i].split(' ')[0]),int(cases[i].split(' ')[1])
        count += 1
        result.write('Case #%s:\n' % (count))
        mat = []
        for j in range(i+1,i+R+1):
            temp = list(cases[j])
            mat.append(temp)
        ca = cake(mat)
        for k in range(len(ca)):
            r = ''.join(ca[k])+'\n'
            result.write(r)
        i = i + R + 1
    result.close()
    
main()
    
        