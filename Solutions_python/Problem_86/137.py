#!/usr/bin/python

import sys

def Solve():
    [n, l, h] = map(int,sys.stdin.readline().split())
    notes = map(int,sys.stdin.readline().split())
    for jeff_note in range(l, h+1):
        freq = True
        for i in notes:
            if i % jeff_note != 0 and jeff_note % i != 0:
                freq = False
                break
        if freq == True:
            return jeff_note
        
    return "NO"

num = int(sys.stdin.readline())

for case in range(1, num + 1):
    print "Case #%d: %s" % (case, Solve())
