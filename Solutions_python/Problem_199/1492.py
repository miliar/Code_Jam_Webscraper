# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def toggle(c):
    if c == '+':
        return '-'
    elif c == '-':
        return '+'

inp = open('A-large.in','r')
t = int(inp.readline())
cases = [inp.readline()[:-1] for s in range(t)]

for c in range(t):
    error = 0
    count = 0 
    line = cases[c].split(" ")
    k = int(line[1])
    for x in range(len(line[0])-k+1):
        if line[0][x] == '-':
            line[0] = line[0][:x] + ''.join([toggle(y) for y in line[0][x:x+k]]) + line[0][x+k:]
            count += 1

    for x in range(len(line[0])):
        if line[0][x] == '-':
            error = 1

    if (error):       
        print("Case #{}: {}".format(c+1, 'IMPOSSIBLE'))
    else:
        print("Case #{}: {}".format(c+1, count))
        