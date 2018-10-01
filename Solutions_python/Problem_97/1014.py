#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

inputFile = open('in.txt', 'r', encoding='utf-8')
outputFile = open('output.txt', 'w', encoding='utf-8')

T = int(inputFile.readline().strip())
for _ in range(T):
    line = inputFile.readline().strip().split(' ')
    line = [int(value) for value in line]
    A = line[0]
    B = line[1]

    pair = set()
    
    bStartNum = int(str(B)[0])
    for no in range(A, B + 1):
        s = str(no)
        
        for i in range(1, len(s)):
            startNum = int(s[-i])
            if startNum == 0:
                continue
            if startNum < bStartNum:
                newNum = int(s[-i:] + s[:-i])
                if A <= newNum <= B:
                    if no != newNum:
                        pair.add(str(min(no, newNum)) + '-' + str(max(no, newNum)))
            else:
                newNum = int(s[-i:] + s[:-i])
                if A <= newNum <= B:
                    if no != newNum:
                        pair.add(str(min(no, newNum)) + '-' + str(max(no, newNum)))
    
    
    # delete number like '1111' '2222'
    for i in range(len(str(A)), len(str(B)) + 1):
        for j in range(1, 10):
            if A <= int(str(j) * i) <= B:
                #print('--'+str(j) * i)
                pair.discard(str(j) * i + '-' + str(j) * i)

    outputFile.write("Case #" + str(_ + 1) + ": " + str(len(pair)) + "\n")
    
outputFile.close()