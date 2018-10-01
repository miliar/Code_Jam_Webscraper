#!/usr/bin/env python

import re

def splitpar(s):
    c = 0
    for i in range(len(s)):
        if s[i] == '(':
            c += 1
        elif s[i] == ')':
            c -= 1
        if c == 0:
            return s[:i+1], s[i+1:]

r = re.compile('\(\s*(\d+(?:\.\d+)?)\s*(\w*)\s*(.*)\)')

def znova(a, s, p):
    tree = r.findall(s)[0]
    pravdepodobnost = tree[0]
    vlastnost = tree[1]
    dalsi = splitpar(tree[2])
    p *= float(pravdepodobnost)
    if vlastnost:
        if vlastnost in a:
            return znova(a, dalsi[0], p)
        else:
            return znova(a, dalsi[1], p)
    else:
        return p

if __name__ == '__main__':


    N = int(raw_input())
    for i in range(N):
        print "Case #%d: " % (i+1)
        L = int(raw_input())
        
        s = ""
        for j in range(L):
            s += raw_input()

        A = int(raw_input())
        for k in range(A):
            animal = raw_input().split()[2:]
            print "%.8f" % znova(animal, s, 1)



            



