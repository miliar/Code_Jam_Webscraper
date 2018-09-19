#!/usr/bin/env python
import sys

if __name__ == '__main__':
    
    fh = file(sys.argv[1], 'r')
    n = int(fh.readline())
    for i in range(n):
        line = fh.readline().split()
        C = float(line[0])
        F = float(line[1])
        X = float(line[2])
        
        prod = 2.0
        time = 0.0
        
        while True:
            timefarm = C / prod
            timewin = X / prod
            
            if timefarm + X / (prod + F) < timewin:
                time += timefarm
                prod += F
                
            else:
                time += timewin
                break
                
        print 'Case #%d: %.7f' %(i+1, time)
        
        
