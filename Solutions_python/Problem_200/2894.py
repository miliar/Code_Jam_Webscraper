# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:18:26 2017

@author: Tom
"""


import sys

# Tidy Numbers CodeJam challenge


def isTidy(v):
    # Figure out if this number is tidy
    s = str(v)
    if len(s) > 1:
        for k in range(1,len(s)):
            if s[k] < s[k-1]:
                return False
    
    return True



# read the filename from the argument
if len(sys.argv) > 1:
    filepath = sys.argv[1]
else:
    filepath = input("Enter filename: ")

outfile = filepath + ".out"

# open the file
with open(filepath,'r') as f:
    
    # read the first line of the file for the number of test cases
    T = int(f.readline())
    
    # read all the test cases into a list
    Nlist = []
    for c in range(T):
        Nlist.append(int(f.readline()))
    
    # for each case, find the last tidy number
    R = []
    for N in Nlist:
        print("Trying case {}".format(N))
        for v in range(N,-1,-1):
            if(isTidy(v)):
                R.append(v)
                print("Found tidy number {}".format(v))
                break
    
    # writing output file
    with open(outfile,'w') as o:
        for x,y in enumerate(R):
            s = "Case #{}: {}".format(x+1,y)
            print(s)            
            o.write(s+'\n')
            
