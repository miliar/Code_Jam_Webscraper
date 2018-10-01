'''
Created on May 7, 2010

@author: gustavo
'''

import os
import sys
import string

if __name__ == '__main__':
    

    fpIn = open(sys.argv[1], 'rt')
    fpOut = open('out', 'wt')
    #fpOut = sys.stdout
    
    lines = fpIn.readlines()
    
    numCases = int(lines[0])
    
    caseNum = 1
    for i in xrange(1, numCases*2, 2):
        
        case = lines[i].rstrip()
        
        case = map(int, case.split(' '))
        
        R = case[0]
        k = case[1]
        N = case[2]
        
        case = lines[i+1].rstrip()
        group = map(int, case.split(' '))
    
        money = 0
        for t in xrange(R):
            
            newGroup = []
            oldGroup = group[:]
            numPeople = 0
            for j in group:
                                
                if (numPeople+j) > k:
                    for x in reversed(oldGroup):
                        newGroup.insert(0, x)
                    break
                
                numPeople += j
                newGroup.append(j)
                oldGroup = oldGroup[1:]               
            
            money += numPeople   
            group = newGroup
                
        
        fpOut.write('Case #%d: ' % int(caseNum) + str(money) + '\n'  ) 
        caseNum += 1
    
    fpIn.close()
    fpOut.close()            
        
