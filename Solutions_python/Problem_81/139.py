#!/usr/bin/env python
import sys
from numpy import *

def read_n(a):
    n = int(a[0])
    return a[1:n+1], a[n+1:]

def solve():
    N = int(sys.stdin.readline())
    a = [sys.stdin.readline().strip() for i in range(N)]
    num = [i.count('0') + i.count('1') for i in a]
    win = [i.count('1') for i in a]
    OWP = [sum((
                (win[j] - int(a[j][i]=='1')) / float(num[j]-1)
               for j in range(N) if a[i][j]!='.')) / float(num[i])
           for i in range(N)]
    # print
    # print win
    # print num
    # print [[(win[j] - int(a[j][i]=='1')) / float(num[j]-1)
    #         for j in range(N) if a[i][j]!='.']
    #        for i in range(N)]
    # print OWP
    # print [[1.*win[i]/num[i],
    #         OWP[i],
    #         sum((OWP[j] for j in range(N) if a[i][j]!='.'))/num[i]]
    #         for i in range(N)]
    # print 

    return [0.25*win[i]/num[i]
            + 0.5 * OWP[i]
            + 0.25 * sum((OWP[j] for j in range(N) if a[i][j]!='.'))/num[i]
            for i in range(N)]


if __name__=="__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        print "Case #{}:".format(t+1)
        print "\n".join(map(str,solve()))

