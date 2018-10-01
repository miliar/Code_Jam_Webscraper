#!/usr/bin/env python
import sys

case = 0

def flip(array):
    return ['+' if i=='-' else '-' for i in array]

def moves(pancakes,k):
    if pancakes=='+'*len(pancakes):
        print 'Case #'+str(case)+': ' + str(0)
    else:
        m=0;pancakes = list(pancakes)
        for i in range(len(pancakes)-k+1):
            if pancakes[i] == '-':
                pancakes = pancakes[:i]+flip(pancakes[i:i+k])+pancakes[i+k:]
                m+=1
        
        if pancakes==['+']*len(pancakes):
            print 'Case #'+str(case)+': ' + str(m)
        else:
            print 'Case #'+str(case)+': IMPOSSIBLE'
  
sys.stdin.readline()
for line in sys.stdin:
    case += 1
    x = line.split()
    moves(x[0],int(x[1]))
