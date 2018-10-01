#!/usr/bin/python

import sys

def solve_case():
    plates_count=sys.stdin.readline()
    pancakes=[int(n) for n in sys.stdin.readline().split(" ")]
    time_past=0

    best=max(pancakes)
    for new_max in range(1,best):
        cost=0
        for x in pancakes:
            if x>new_max:
                cost+=x/new_max-1
                if x%new_max>0:
                    cost+=1
        if new_max+cost<best:
            best=new_max+cost
    return `best`

cases_count=int(sys.stdin.readline())

for i in xrange(cases_count):
    print "Case #"+`i+1`+": "+solve_case()

