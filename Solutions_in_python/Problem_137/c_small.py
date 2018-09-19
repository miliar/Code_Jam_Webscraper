#!/usr/bin/env python

import json

f = open('c_small_data.json')
d = f.read()
f.close()
X = json.loads(d)

N = int(raw_input())
for i in range(N):
    L = raw_input()
    V = L.split()
    R = V[0]
    C = V[1]
    M = V[2]
    print 'Case #' + str(i+1) + ': '
    for k in X.keys():
        if R == X[k]["p"][0] and C == X[k]["p"][1] and M == X[k]["p"][2]:
            for l in X[k]["a"]:
                l = l.rstrip()
                print l
    #solve(R, C, M)


