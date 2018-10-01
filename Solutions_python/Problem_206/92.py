#!/usr/bin/env python

def nextline():
    return [int (s) for s in input().split(' ')]

t = int(input())
for i in range(1, t+1):
    d, n = nextline()
    max_t = 0
    for j in range(n):
        horse = nextline()
        t = (d - horse[0])/horse[1]
        if t > max_t:
            max_t = t
    print(f'Case #{i}: {d/max_t}')






