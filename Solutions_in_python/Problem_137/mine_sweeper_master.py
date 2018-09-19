# -*- coding: utf-8 -*-
"""
Solves the 'Mine Sweeper Master' Problem Google Code Jam Qualifications 2014

https://code.google.com/codejam/contest/2974486/dashboard#s=p1

Created on Sat Apr 12 10:35:51 2014

@author: Luca
"""
import numpy as np
import sys

def place_mines(grid,M):
    cnt = 0
    if M==0:
        grid[-1,-1]=2
        return grid
        
    for i in range(0,grid.shape[0]):
        for j in range(0,grid.shape[1]):
           grid[i,j]=1
           cnt +=1
           if cnt==M:
               grid[-1,-1]=2
               return grid

def place_mines2(grid,M):
    cnt = 0
    if M==0:
        grid[-1,-1]=2
        return grid
    R = grid.shape[0]
    C = grid.shape[1]
    i = 0
    j= 0    
    res_R = R
    res_C = C
    if R>=C:
        ins_order = 'r'
    else:
        ins_order = 'c'    
    while cnt<M:
        if ins_order == 'r':
            grid[i,j]=1
            j=j+1
            cnt +=1
            if j>=C  or (j==C-2 and cnt==M-1 and res_R>0):
                res_R-=1
                j=C-res_C
                i+=1
                if res_R<res_C:
                    ins_order = 'c'
                    j=C-res_C
                    i=R-res_R    
                continue    
        if ins_order == 'c':
            grid[i,j]=1
            i=i+1
            cnt +=1
            if i>=R or (i==R-2 and cnt==M-1 and res_C>0):
                res_C-=1
                i = R-res_R
                j+=1
                if res_C<res_R:
                    ins_order = 'r' 
                    j=C-res_C
                    i=R-res_R    
                continue    
        
        
    grid[-1,-1]=2
    return grid
              
def get_neigh(CN,R,C):
    increments = np.array([[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]],dtype=np.int)
    D = CN + increments
    test=np.logical_and(np.logical_and(D[:,0]>=0,D[:,0]<=R),np.logical_and(D[:,1]>=0,D[:,1]<=C))    
    return D[test]
      
def check_solution(grid):
    C = np.where(grid==2)
    CN = np.array([C[0][0],C[1][0]])
    answer = grid*0-1
    # Perform Flood Fill from C
    R = grid.shape[0]-1
    C = grid.shape[1]-1
    visited = grid*0
    grid[CN[0],CN[1]]=0
    fringe = [CN]
    while len(fringe)>0:
        CN = fringe[-1]
        fringe = fringe[0:-1]
        if grid[CN[0],CN[1]]==1:
            continue
        # Consider neighbours of CN
        neigh = get_neigh(CN,R,C)
        mines = np.sum(grid[neigh[:,0],neigh[:,1]])
        answer[CN[0],CN[1]]=mines
        visited[CN[0],CN[1]]=1
        for t in neigh:
            if visited[t[0],t[1]]==0 and answer[CN[0],CN[1]]==0:
                fringe.append(t)   
    return answer    
if __name__ == '__main__':

    if len(sys.argv)<2:
        print 'Need to specify an input file'
        exit(1)

    input_file = sys.argv[1]
    output_file =  'mine_sweeper_master_output_6.txt'    
    do_debug = False
    
    symbol_map = ['.','*','c']

    try:
      with open(input_file,'r') as f:
        lines = f.readlines()
        T = int(lines[0])
        print 'Solving Mine Sweeper Master Problem T=%d test cases.'%(T)
        data  = [] # List of R,C,M  
        for n in range(0,T):
            data.append( [int(t) for t in lines[n+1].strip('\n').split()])
            if do_debug:
                print 'Test case %d'%(n+1)
                print 'R=%d,C=%d,M=%d'%(data[n][0],data[n][1],data[n][2])
                
    except IOError:
       print 'File %s not found'%input_file
       exit(1)       
    solution = []   
    for n in range(0,T):
        R = data[n][0]
        C = data[n][1]
        M = data[n][2]
        print 'Solving Mine Sweeper Master Problem R=%d,C=%d,M=%d'%(R,C,M)
        grid = np.zeros((R,C),dtype= np.int)
        grid = place_mines2(grid,M)      
        #print 'Calculated grid:'
        #print 'Solution check:'
        
        tst = check_solution(grid)
        grid[-1,-1]=2        
        # Test if successful all -1 should coorrespond to mines
        # initial point position should have 0
        if (np.max(np.logical_and(tst==-1,grid!=1))==False):
            sol = ''                
            for m in range(0,R):
                sol = sol+ ''.join([symbol_map[t] for t in grid[m,:]])+ '\n'
            solution.append(sol)    
        else:
           solution.append('Impossible\n')
        #print solution[-1]
        #print tst
    try:
      with open(output_file,'w') as f:
          for n in range(0,T):
              f.write('Case #%d:\n'%(n+1))
              f.write(solution[n])
    except IOError:
       print 'File %s not found'%output_file
       exit(1)