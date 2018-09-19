'''
Created on May 7, 2010

@author: gustavo
'''

import os
import sys
import string
import numpy

ON = 1
OFF = 0
POWER = 2

if __name__ == '__main__':
    

    fpIn = open(sys.argv[1], 'rt')
    fpOut = open('out', 'wt')
    #fpOut = sys.stdout
    
    lines = fpIn.readlines()
    
    numCases = int(lines[0])
    
    for i in xrange(1, len(lines)):
        
        case = lines[i].rstrip()
        
        case = map(int, case.split(' '))
        N = case[0]
        K = case[1] 
    
        snappers = numpy.ndarray(shape=(N+1), dtype=numpy.int32)
        snappers.fill(0)
        snappers[0] = POWER
        for j in xrange(K):
            
            for k in xrange(N):
            
                if snappers[k] & POWER:
                    snappers[k] ^= ON
                else:
                    break
                
            for k in xrange(1, N):
                 
                if (snappers[k-1] & ON) and (snappers[k-1] & POWER):
                    snappers[k] |= POWER
                else:
                    snappers[k] &= ~POWER
                                               
        if (snappers[N-1] & ON) and (snappers[N-1] & POWER):
            case = 'ON'
        else:
            case = 'OFF'
            
        fpOut.write('Case #%d: ' % int(i) + case +'\n'  ) 
    
    fpIn.close()
    fpOut.close()            
        
