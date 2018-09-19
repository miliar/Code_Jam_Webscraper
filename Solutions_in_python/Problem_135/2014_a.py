#!/usr/bin/python

import pickle
import sys
import os

def common(row1,row2):
    n=0
    c=None
    for i in row1:
        for j in row2:
            if i==j:
                n=n+1
                c=i
    return (n,c)

if len(sys.argv) < 2:
  quit()

f = open(sys.argv[1],'r')
fout = open("fout.txt","w")
N = int(f.readline()) #number of test cases
for t in range(N):
    r1 = int(f.readline()) # first row
    for i in range(4):
        line=f.readline()
        if i+1==r1:
            row1=map(int,line.strip().split())
    r2 = int(f.readline()) # second row
    for i in range(4):
        line=f.readline()
        if i+1==r2:
            row2=map(int,line.strip().split())

    (n,c)=common(row1,row2)
    if n==1:
        fout.write("Case #"+str(t+1)+": "+str(c))
    elif n==0:
        fout.write("Case #"+str(t+1)+": Volunteer cheated!")
    elif n>1:
        fout.write("Case #"+str(t+1)+": Bad magician!")
    fout.write("\n")
  
