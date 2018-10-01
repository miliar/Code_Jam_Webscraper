#!/usr/bin/python

import os
import sys
import math

fn = sys.argv[1]

fh = open(fn, "r")
T = int(fh.readline().strip())
cases = []

for i in range(T):
    case = {}
    [A, N] = map(int, fh.readline().strip().split())
    case["A"] = A
    case["N"] = N
    ns = map(int, fh.readline().strip().split())
    case["ns"] = ns
    cases.append(case)

fh.close()

#print cases


def determine_case(case):
    A = case["A"]
    N = case["N"]
    ns = case["ns"]
    ns.sort()
    vals = [0]+ns
    edits = [[] for i in range(N+1)]
    edits[0] = [[0,A]]
    print "new", edits, A, N, ns
    for i in range(N):
        pos = i+1
        m = ns[i]
        print ">>", m
        for start in edits[pos-1]:
            ed = start[0]
            val = start[1]
            if m < val:
                edits[pos].append([ed, val+m])
            else:
                try:
                    new_e = int( math.ceil( math.log((m-1.0)/(val-1.0))/math.log(2.0) ))
#int(math.ceil((m-1.0)/(2.0*(val-1))))
                    if new_e == 0:
                        print "LOOK", m, val
                        #dummy = dummy1
                        new_e = 1
                    if int(math.pow(2,new_e)*val-math.pow(2,new_e)+1) == m:
                        new_e += 1
                    new_v = int(math.pow(2,new_e)*val-math.pow(2,new_e)+1) + m
                    print "E", m, val, new_e, new_v
                    edits[pos].append([new_e+ed, new_v])
                except:
                    pass
                edits[pos].append([ed+1, val])
        print i, edits
        cleaned_edits = []
        for ed in list(set([j[0] for j in edits[pos]])):
            cleaned_edits.append([ed, max(j[1] for j in edits[pos] if j[0]==ed)])
        edits[pos] = cleaned_edits
    print edits[-1]
    return str(min([i[0] for i in edits[-1]]))

fh_o = open("out2.txt","w")
for i, case in enumerate(cases):
    print >> fh_o, "Case #"+str(i+1)+": "+ determine_case(case)


fh_o.close()

