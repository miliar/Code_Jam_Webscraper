# -*- coding: utf-8 -*-
"""
Solves the 'Cookie Clicker Alpha' Problem Google Code Jam Qualifications 2014

https://code.google.com/codejam/contest/2974486/dashboard#s=p1

Created on Fri Apr 12 1:58:51 2014

@author: Luca
"""
import numpy as np
import sys

def get_childern(node,C,F,X):
    if (node(1)+C)>X:
        child_no_fact = (node(0)+(X-node(1))/node(2),X,node(2))
        return [child_no_fact]
    child_no_fact = (node(0)+C/node(2),node(1)+C,node(2))
    child_fact = (node(0)+C/node(2),node(1),node(2)+F)
    return [child_no_fact,child_fact]
   
def solve_cookie_clicker_alpha(C,F,X):
    root = (0,0,2) # time,cookies,rate
    current_node = root
    
    fringe = [root]
    visited = []
    solution = []
    while len(fringe)>0:
        current_node = fringe[0]
        ch = get_children(current_node)
        for c in ch:
            if c not in visited:
                fringe.append(c)
        if fringe[-1](1)==X:
            solution.append(fringe[-1])
            visite.append()

def solve_by_enumeration(C,F,X):
    # Trivial solution
    rate =2.0
    min_time = X/rate
    last_time = min_time 
    n = 1
    #print 'Trivial solution no farms %f'%(min_time)    
    while True:
        # Buy a farm whenever is possible
        # We assume intermediate solution when the farm is bought 
        # After it was possible are sub optimal
        rate = 2.0
        time = 0.0
        #print 'Solution buying %d farms'%(n)    
        for i in range(0,n):
            time += C/rate
            #print 'Farm %d bought at time %f'%(i+1,time)            
            rate += F
        time +=X/rate
        #print 'Final time %f'%(time)            
        if time<min_time:
            min_time = time
        else:
            return min_time            
        n = n +1 
            
    return min_time    

if __name__ == '__main__':

    if len(sys.argv)<2:
        print 'Need to specify an input file'
        exit(1)

    input_file = sys.argv[1]
    output_file =  'cookie_clicker_alpha_output_3.txt'    
    do_debug = True
    
    try:
      with open(input_file,'r') as f:
        lines = f.readlines()
        T = int(lines[0])
        print 'Solving Cookie Clicker Alpha Problem for T=%d test cases.'%(T)
        data  = np.zeros((T,3),dtype=np.float64)  
        for n in range(0,T):
            data[n,:] = np.array([float(t) for t in lines[n+1].split()],dtype = np.float)
            if do_debug:
                print 'Test case %d'%(n+1)
                print 'C,F,X=%f,%f,%f'%(data[n,0],data[n,1],data[n,2])
                
    except IOError:
       print 'File %s not found'%input_file
       exit(1)       

    # Solve the problem use binary tree depth first search
    # tree branching every time a factory can be bought
    solutions = []
    for n in range(0,T):
        C,F,X = data[n,:]       
        print 'Solving Cookie Clicker Alpha Problem %d C,F,X=%f,%f,%f'%(n,C,F,X)
        
       
        res = solve_by_enumeration(C,F,X)   
        solutions.append(res)
    try:
      with open(output_file,'w') as f:
          for n in range(0,T):
              f.write('Case #%d: %12.8e\n'%(n+1,solutions[n]))
    except IOError:
       print 'File %s not found'%output_file
       exit(1)