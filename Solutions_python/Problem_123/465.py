#!/usr/bin/python

import re
import sys
from string import maketrans

input_file = open('A-large.in')
output_file = sys.stdout#open('A-large.out', 'w')

T = int(input_file.readline())

def num_delete_ops(i, length):
    return length - i

def num_insert_ops(A, size):
    result = 0
    while A <= size:
        A = A*2-1
        result += 1
    return result, A

for t in range(T):
    (A, N) = map(int, input_file.readline().split(' '))
    motes = map(int, input_file.readline().split(' '))
    
    if A == 1:
        num_ops = len(motes)
    else:
        motes.sort()
        num_ops = 0
        
        i = 0
        length = len(motes)
        lowest = len(motes)
        while i < length: 
        
            if motes[i] < A:
                A += motes[i]
                i += 1
            else:
                ndo = num_delete_ops(i, length)
                nio, tmp = num_insert_ops(A, motes[i])
                lowest = min(lowest, ndo+num_ops)
                if lowest <= nio+num_ops:
                    num_ops = lowest
                    break
                else:
                    A = tmp
                    num_ops += nio
    
    result = str(num_ops)
    output_file.write("Case #" + str(t + 1) + ": " + result + "\n")
    

input_file.close()
output_file.close()
