#!/usr/bin/env python

import sys
case = 0
def print_results(*args,**kwargs):
    print 'Case #'+str(case)+': '+' '.join(*args)

def solution(D,N,other_horses):
    other_horses.sort(key = lambda x:x[0])
    finish_time = (D-other_horses[-1][0])/other_horses[-1][1]
    
    for i,e in enumerate(other_horses[::-1]):
        finish_time = max(finish_time,(D-e[0])/e[1])
    print_results([str(D/finish_time)])
testcases = int(sys.stdin.readline())

for i in range(testcases):
    case += 1
    x,y = sys.stdin.readline().split()
    x,y = int(x), int(y)
    solution(x,y,[map(float,sys.stdin.readline().split()) for j in range(y)])
