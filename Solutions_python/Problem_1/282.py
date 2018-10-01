#!/usr/bin/python
#
# Google Code Jam 2008
# Submission: nicholas.cw.ng@gmail.com

def zero_dict(key):
    ses[key] = 0

import sys
n = int(sys.stdin.readline()) # number of cases

for case in range(0, n): # cases
    s = int(sys.stdin.readline()) # number of search engines
    switch = 0
    ses = dict()
    for se in range(0, s): # search engines
        ses[sys.stdin.readline().rstrip()] = 0

    q = int(sys.stdin.readline()) # number of queries
    for query in range(0, q): # queries
        qstr = sys.stdin.readline().rstrip()
        
        if len(filter(lambda key: ses[key]==0, ses))==1 and ses[qstr]==0:
            switch += 1 # we need to switch
            for k in ses:
                ses[k] = 0
        ses[qstr] += 1

    print "Case #"+str(case+1)+":",switch
