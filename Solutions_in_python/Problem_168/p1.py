#!/usr/bin/python3 -OO
import math,string,itertools,fractions,re,array,bisect
import numpy as np
from heapq import *
from collections import *

dirs = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}

for cas in range(1,int(input())+1):
    r,c = map(int,input().strip().split())
    grid = np.array([list(input().strip()) for _ in range(r)])
    visited = np.zeros(grid.shape, dtype=bool)
    def calc():
        t = 0
        for y in range(r):
            for x in range(c):
                if grid[y,x] != '.' and not visited[y,x]:
                    dy,dx = dirs[grid[y,x]]
                    visited[y,x] = True
                    cy,cx = y+dy,x+dx
                    while 0<=cy<r and 0<=cx<c and not visited[cy,cx]:
                        if grid[cy,cx] != '.':
                            visited[cy,cx] = True
                            dy,dx = dirs[grid[cy,cx]]
                        cy,cx = cy+dy,cx+dx
                    if not (0<=cy<r and 0<=cx<c):
                        cy,cx = cy-dy,cx-dx
                        while grid[cy,cx] == '.':
                            cy,cx = cy-dy,cx-dx
                        dy,dx = dirs[grid[cy,cx]]
                        #print(cy,cx)
                        for k,v in dirs.items():
                            _dy,_dx = v
                            if k == grid[cy,cx]: continue
                            ey,ex = cy+_dy,cx+_dx
                            while 0<=ey<r and 0<=ex<c and grid[ey,ex] == '.':
                                ey,ex = ey+_dy,ex+_dx
                            if (0<=ey<r and 0<=ex<c):
                                #print(k,ey,ex,grid[ey,ex])
                                grid[cy,cx] = k
                                t += 1
                                break
                        else:
                            print('Case #%d: IMPOSSIBLE'%cas)
                            return
                            
        #print(grid)
        print('Case #%d: %d'%(cas,t))
    calc()
