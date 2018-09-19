'''
Created on May 7, 2010

@author: kapild
'''

from math import pow

def SnapperChain(fileName):
    
    fr = open(fileName)
    
    lines = fr.readline()
    
    input = fr.readlines()
    
    
    
    for i in range(int(lines)):
        input_line = input[i].split(" ")
        
        n = int(input_line[0])
        k = int(input_line[1])
        
        sum = pow(2,n)
        result = sum -1 
        
        if ( (k - result) % sum == 0):
            print "Case #" + str(i+1) + ": ON"
        else:
            print "Case #" + str(i+1) + ": OFF"
            
    

if __name__ == '__main__':

    SnapperChain("file1.txt")