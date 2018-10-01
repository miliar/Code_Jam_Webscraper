#!/usr/bin/python

import sys

T = input ()

for Tc in range (1, int(T)+1):
    
    N = input ()
    loop = True
    
    while (loop):   
        
        loop = False
        
        X = ''
        
        if len(N) == 1:
            X = N
        
        for i in range (0, len(N)-1):
            # len(N)=6, i=0,1,2,3,4 [5]

            j = i+1

            if N[i] <= N[j]:
                X += N[i]

                if i==len(N)-2:
                    X += N[j]

                continue

            X += str(int(N[i]) - 1)[0]

            for j in range (i+1, len(N)):
                X += '9'

            loop = True
                
            break
        
        N = X
    
    # exclude leading zeros
    while N.startswith('0'):
        N = N[1:]
    
    print ('Case #' + str(Tc) + ': ' + N)
    