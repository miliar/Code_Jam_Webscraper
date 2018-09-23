# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:05:00 2017

@author: Tom
"""


import sys
import collections


# Bathroom Stalls CodeJam challenge

# read the filename from the argument
if len(sys.argv) > 1:
    filepath = sys.argv[1]
else:
    filepath = input("Enter filename: ")

outfile = filepath + ".out"

# open the file
with open(filepath,'r') as f:
    with open(outfile,'w') as o:
    
        # read the first line of the file for the number of test cases
        f.readline()
        
        # read all the test cases into a list
        caseNumber = 1
        for line in f:
            N,K = line.split(' ')
            N = int(N)
            K = int(K)
            print('Testing case #{}:  {}, {}'.format(caseNumber,N,K))
            
            gaps = collections.OrderedDict()
            gaps[N] = 1
            
            # Loop for each person??
            for k in range(K):
                # find leftmost biggest gap
                for size,number in gaps.items():
                    if number > 0:
                        break
                
                # Subtract one from the count of this largest gap
                if number == 1:
                    del gaps[size]
                else:
                    gaps[size] = gaps[size] - 1
                
                # Add the two smaller gaps just created
                if size % 2 == 1:
                    # if gap is odd in width, two new gaps of (g-1)/2 are created
                    g = int((size-1)/2)
                    if g in gaps:
                        gaps[g] = gaps[g] + 2
                    else:
                        gaps[g] = 2
                else:
                    # if gap is even, smaller remainder comes first
                    g = int(size/2)
                    if g in gaps:
                        gaps[g] = gaps[g] + 1
                    else:
                        gaps[g] = 1
                    g = g-1
                    if g in gaps:
                        gaps[g] = gaps[g] + 1
                    else:
                        gaps[g] = 1
                
            
            g = size
            if g % 2 == 1:
                # if gap is odd in width, two new gaps of (g-1)/2 are created
                minDist = int((g-1)/2)
                maxDist = int((g-1)/2)
            else:
                # if gap is even, smaller remainder comes first
                minDist = int((g/2)-1)
                maxDist = int(g/2)
            
            print('All done!  Answer: {} {}'.format(maxDist,minDist))
            o.write('Case #{}: {} {}\n'.format(caseNumber,maxDist,minDist))
            caseNumber = caseNumber + 1