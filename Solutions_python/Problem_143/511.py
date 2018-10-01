# -*- coding: utf-8 -*-

from pylab import *
import numpy

infile = open('input.txt', 'r')
outfile = open("task2-output.txt", "w")

numcases = int(infile.readline())

for case in range(0, numcases):
    numbers = infile.readline().split(" ")
    A = int(numbers[0])
    B = int(numbers[1])
    K = int(numbers[2])
    
    print(A,B,K)
    
    T = 0
    for i in range(0, A):
        for j in range(0, B):
            if (i & j < K):
                T += 1
    
    print('Case #',(case+1),': ',T)
    outfile.write('Case #'+str(case+1)+': '+str(T)+'\n')
    
        

outfile.close()
    

