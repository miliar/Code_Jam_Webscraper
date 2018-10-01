#!/usr/bin/env python
'''
Created on Apr 14, 2012

@author: san
'''
import sys

def is_recycled(a,b):
    if a.startswith('0') or b.startswith('0') :
        return 0
    for i in range(1,len(a)):
        if a[i:]+a[:i] == b:
            return 1
    return 0

def main():
        input_file = open(sys.argv[1])
        output_file = open(sys.argv[2], 'w')
        no_cases = int(input_file.readline())
        for k in range(no_cases):
            [A,B] = input_file.readline().split()
            iA = int(A)
            iB = int(B)
            count = 0
            for i in range(iA,iB+1):
                for j in range(i+1,iB+1):
                    count = count + is_recycled(str(i),str(j))
            output_file.write('Case #' + str(k + 1) + ': ')
            output_file.write(str(count)+'\n')
        input_file.close()
        output_file.close()
        

if __name__ == '__main__':
    main()