#!/usr/bin/env python
import sys

def treatCase(string, string2):
    a = string.split(' ')
    a = [int(i) for i in a]
    P,K,L = a

    if L > P*K:
        return "impossible"

    a = string2.split(' ')
    a = [int(i) for i in a]
    a.sort(reverse=True)

    k=0
    keypad=[[] for i in range(K)]
    for i in range(len(a)):
        keypad[k].append(i)
        k+=1
        if k>=K: k=0

    press=0
    for i in range(len(a)):
        for j in keypad:
            if i in j:
                press += (j.index(i)+1)*a[i]

    return press

if len(sys.argv) == 2:
    file = open(sys.argv[1])
else:
    file = open('sample')

lines = file.readlines()
file.close

lines = [line.split('\n')[0] for line in lines]
cases = int(lines[0])

for case in range(2,cases*2+1,2):
    print "Case #"+str(case/2)+": "+str(treatCase(lines[case-1], lines[case]))
