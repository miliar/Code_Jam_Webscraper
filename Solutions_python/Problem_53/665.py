'''
Created on May 8, 2010

@author: jmvieira
'''

import sys

f_in = open(sys.argv[1], 'r')
f_out = open(sys.argv[2], 'w')

T = int(f_in.readline())

for case_n in range(1, T + 1):
    test = f_in.readline().split()
    N = int(test[0])
    K = float(test[1])
    
    on = 1
    
    if N > 1:
        on = (2 ** N) - 1
    
    state = 'OFF'

    if K > 0:
        if K % (on + 1) == on:
            state = 'ON' 
    
    f_out.write('Case #%d: %s\n' % (case_n, state))