# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 17:52:06 2017

@author: Robbe Sneyders
"""

def answer(d, horses):
    
    slowest = 0
    for horse in horses:
        time = (d - horse[0]) / horse[1]
        slowest = max(time, slowest)
        
    speed = d/slowest
    return speed
        
    

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    d, n = [int(s) for s in input().split(" ")]
    
    horses = []
    for j in range(n):
        horses.append([int(s) for s in input().split(" ")])
        
    speed = answer(d, horses)
    print("Case #{}: {}".format(i, speed))