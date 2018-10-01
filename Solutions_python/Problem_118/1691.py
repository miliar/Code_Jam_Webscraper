#!c:\Python33\python.exe
# vim:fileencoding=utf-8

import sys
import re
import glob
import itertools
from math import sqrt
import pdb


def in_out():
    infiles = glob.glob("*.in")
    for infile in infiles:
        keyword = (sys.argv[1] if len(sys.argv)>1 else "test")
        if re.search(keyword, infile):
            return (open(infile,"r"), open(infile[:-2]+"out", "w+"))

def fair(n):
    x=str(n)
    L=len(x)//2
    for l in range(L):
        if not x[l] == x[0-l-1]:
            return False
    return True

def main():
    fin,fout = in_out()
    casenum = int(fin.readline()[:-1])
    for i in range(casenum):
        A,B=fin.readline()[:-1].split()
        A=int(A)
        B=int(B)
        a=sqrt(A)
        b=sqrt(B)
        a=int(a)+1 if int(a)<a else int(a)
        b=int(b)
        y=0
        for j in range(a,b+1):
            if fair(j) and fair(j*j):
                y+=1

        fout.write('Case #'+str(i+1)+": "+str(y)+"\n")

    fout.flush()
    fout.seek(0)
    print(fout.read())

if __name__ == "__main__":
    main()

