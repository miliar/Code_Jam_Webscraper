#!/usr/bin/python

import os

import sys


fn = sys.argv[1]

fh = open(fn, "r")
T = int(fh.readline().strip())
cases = []
for i in range(T):
    case = map(int, fh.readline().strip().split(" "))
    cases += [case]

fh.close()

fh_o = open("out.txt","w")
for i in range(T):
    case = cases[i]
    N = case[0]
    S = case[1]
    p = case[2]
    tots = case[3:]
    print "\n", N, S, p, tots
    lows = map(lambda x: x/3, tots)
    extras = map(lambda x: x%3, tots)
    peops = []
    for j in range(N):
        peops += [[lows[j],extras[j]]]
    #print peops
    total_above = []
    pot_sup=[]
    print peops
    #already above
    total_above += filter(lambda x: x[0]>=p, peops)
    print "already", filter(lambda x: x[0]>=p, peops)
    peops = filter(lambda x: x[0]<p, peops)
    #unsuprising above
    total_above += filter(lambda x: x[0]+1>=p and x[1]>0, peops)
    print "unsup  ", filter(lambda x: x[0]+1>=p and x[1]>0, peops)
    peops = filter(lambda x: x[0]+1<p or x[1]==0, peops)
    #potentially suprising, no steal
    pot_sup += filter(lambda x: p<=x[0]+2<=10 and x[1]==2, peops)
    print "potsup", filter(lambda x: p<=x[0]+2<=10 and x[1]==2, peops)
    peops = filter(lambda x: x[0]+2<p or x[0]+2>10 or x[1]!=2, peops)
    #potentially suprising, steal
    pot_sup += filter(lambda x: p<=x[0]+1<=10 and x[1]==0 and x[0]!=0, peops)
    print "potsup", filter(lambda x: p<=x[0]+1<=10 and x[1]==0 and x[0]!=0, peops)
    peops = filter(lambda x: x[0]+1<p or x[0]+1>10 or x[1]!=0 or x[0]==0, peops)
    print >> fh_o, "Case #"+str(i+1)+": "+str(len(total_above)+min([S, len(pot_sup)]))
    print len(total_above), S, len(pot_sup)
    print "Case #"+str(i+1)+": "+str(len(total_above)+min([S, len(pot_sup)]))

fh_o.close()
