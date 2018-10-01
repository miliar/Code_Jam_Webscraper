# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 11:51:27 2017

@author: pellowes
"""


import numpy as np
import sys

fileIn = '/Users/pellowes/test.in'
fileIn = '/Users/pellowes/Downloads/C-small-attempt1.in'
#fileIn = '/Users/pellowes/Downloads/A-large(3).in'
fileOut = fileIn.split('.')[0]+'.out'

f = open(fileIn,'r')
fo = open(fileOut,'w')
    
class Town:
    def __init__(self,num,distances,horseDistance,horseSpeed):
        self.num = num        
        self.timesTo = {}
        self.horseDistance = horseDistance
        self.horseSpeed = horseSpeed
        self.distances = distances
        
    
def solveSimple(n,q,horses,grid,stops):
    
    distanceToNext = []
    distanceToEndAgg = []
    horseDistances = []
    horseSpeeds = []
    
    for horse in horses:
        horseDistances.append(int(horse[0]))
        horseSpeeds.append(int(horse[1]))
    for i in range(0,len(grid)-1):
        distLine = grid[i]
        distanceToNext.append(int(distLine[i+1]))
        distanceToEndAgg.append(-1)
        
    agg = 0
    for j in range(len(distanceToNext)-1,-1,-1):
        agg+= distanceToNext[j]
        distanceToEndAgg[j] = agg
    distanceToEndAgg.append(0)
    
    #print(horses)
    #print(horseDistances)
    #print(horseSpeeds)  
    #print(grid)
    #print(distanceToEndAgg)  
    #print('-----')
    
    bestTimeFrom = []
    for i in range(0,n):
        bestTimeFrom.append(1e99)
    bestTimeFrom[-1]=0
    
    for i in range(n-1,-1,-1):
        #look at all upstream, and try to update them
        for j in range(0,i):
            if(horseDistances[j] >= (distanceToEndAgg[j]-distanceToEndAgg[i])):
                timeBetween = (distanceToEndAgg[j]-distanceToEndAgg[i])/horseSpeeds[j]    
                if(bestTimeFrom[j] > bestTimeFrom[i] + timeBetween):
                    bestTimeFrom[j] = bestTimeFrom[i] + timeBetween
    if(bestTimeFrom[0] > 1e98):
        print(horses)
        print(horseDistances)
        print(horseSpeeds)  
        print(grid)
        print(distanceToEndAgg) 
    return str(bestTimeFrom[0])
    
                

numcases = int(f.readline())
for casenum in range(1,numcases+1):
    problem = f.readline().strip().split(' ')
    n = int(problem[0])
    q = int(problem[1])
    horses = []
    grid = []
    stops = []
    for row in range(0,n):
        horses.append(f.readline().strip().split(' '))
    for row in range(0,n):
        grid.append(f.readline().strip().split(' '))
    for row in range(0,q):
        stops.append(f.readline().strip())
    #print('---')
    fo.write('Case #' + repr(casenum) + ': ' + solveSimple(n,q,horses,grid,stops)+'\n')
    
f.close()
fo.close()