# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 11:04:08 2017

@author: ASUS
"""

FILENAME = 'A-large.in'

def outcome(string, n):
    outcome = 0
    slist = []
    for j in range(len(string)):
        slist.append(string[j])
    while '-' in slist:
        i = slist.index('-')
        if i + int(n) > len(string):
            outcome = 'IMPOSSIBLE'
            break
        for j in range(n):
            if slist[i+j] == '-':
                slist[i+j] = '+'
            else:
                slist[i+j] = '-'
        outcome = outcome + 1
    return outcome

fr = open(FILENAME, 'r')
fw = open('outputAl.txt', 'w')
t = fr.readline()
t = int(t.strip())
cases = fr.readlines()
for i in range(t):
    cases[i] = cases[i].strip().split()
    string = cases[i][0]
    n = int(cases[i][1])
    k = outcome(string, n)
    fw.write("Case #{}: {}\n".format(i+1, k))
fr.close()
fw.close()