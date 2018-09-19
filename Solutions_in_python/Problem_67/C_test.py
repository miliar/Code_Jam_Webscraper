#! /usr/bin/python

#  (c) 2010 Wott (http://wott.net.ru/ , wott@gmail.com)

__author__="Wott"
__date__ ="$05.06.2010 21:18:24$"

import sys
import math

def case(M,s):
    ret = 0
    while max([max(i) for i in M])==1:
        ret+=1
        for i in range(s-1,0,-1):
            for j in range(s-1,0,-1):
                if (M[i][j-1]==0 and M[i-1][j]==0):
                    M[i][j]=0
                if (M[i][j-1]==1 and M[i-1][j]==1):
                    M[i][j]=1
        for j in range(s-1,0,-1):
            if M[0][j-1]==0: M[0][j]=0
        for i in range(s-1,0,-1):
            if M[i-1][0]==0: M[i][0]=0
    return(ret)

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: %s in.file out.file" % sys.argv[0])
        return
    with open(args[0]) as infile:
        with open(args[1],'w') as outfile:
            T = int(infile.readline())
            for t in range(T):
                R = int(infile.readline().rstrip())
                m = [[int (j) for j in infile.readline().rstrip().split()] for i in range(R)]
                s = max([max(i) for i in m])
                M=[[0]*s for i in range(s)]
                for p in m:
                    for i in range(p[0],p[2]+1):
                        for j in range(p[1],p[3]+1):
                            M[j-1][i-1]=1
                c = case(M,s)
                outfile.write("Case #%d: %d\n" % (t+1,c))

if __name__ == '__main__':
    main()
