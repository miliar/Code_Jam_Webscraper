#!/usr/bin/python

import sys

char2q={'i':0, 'j':1, 'k':2}

def solve_case():
    (L,X)=[int(n) for n in sys.stdin.readline().split(" ")]
    string=sys.stdin.readline()[:-1]
    string=X*string
    #print string

    letter=0
    Q=3
    minus=False
    for c in string:
        #print c,
        q=char2q[c]
        if q==Q:
            Q=3
            minus=not minus
        elif Q==3:
            Q=q
        else:
            diff=(3+q-Q)%3
            if diff==1:
                Q=(Q+2)%3
            else:
                Q=(Q+1)%3
                minus=not minus
        if not minus and Q==letter and letter!=3:
            letter+=1
            Q=3
            #print
    if letter==3 and not minus and Q==3:
        return "YES"
    else:
        return "NO"


cases_count=int(sys.stdin.readline())

for i in xrange(cases_count):
    print "Case #"+`i+1`+": "+solve_case()

