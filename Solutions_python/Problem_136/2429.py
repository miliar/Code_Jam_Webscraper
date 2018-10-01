#!/usr/bin/env python

import sys

def Solve(C, F, X):
    cur_best = X/2.0 # trivial
    num_f = 0;
    f_cost = 0.0;
    while(True):
        f_cost += C/(num_f*F + 2.0)
        num_f += 1
        cur_best = min(cur_best, X/(num_f*F + 2.0) + f_cost)
        if(f_cost > cur_best): return cur_best

inp = open(sys.argv[1], 'r').readlines()
T = int(inp[0].strip())
for t in range(T):
    C, F, X = map(float, inp[t+1].strip().split())
    print "Case #"+str(t+1)+": "+str(Solve(C, F, X))



    
