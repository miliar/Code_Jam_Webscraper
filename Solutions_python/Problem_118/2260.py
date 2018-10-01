'''
Created on 13-Apr-2013

@author: PANKAJ JAKHAR
'''
import math
count = 0
def FairandSquare():
    f = open("inputC.txt")
    T = int(f.readline())
    print T
    
    for i in range(T):
#        print 'Test Case: ' + str(i)
        solveFS(f)
        global count
        print 'Case #' + str(i + 1) + ': ' + str(count)
        
def solveFS(f):
    global count
    count = 0
    
    nm = str(f.readline())
    nmlst = nm.split()
    nmInt = map(int, nmlst)
    A = nmInt[0];
    B = nmInt[1];
    for i in range(A, B + 1):
        sqr = math.sqrt(i)
        if math.floor(sqr) - sqr < 0:
            continue
        
        if checkIfPalindrome(str(i)) and checkIfPalindrome(str(int(sqr))):
            global count
            count += 1
            
#        print 'num: ' + str(i)
#        print 'sqrt' + str(math.sqrt(i))
#        checkIfPalindrome(i)
    
    
def checkIfPalindrome(num):
    
    lenNum = len(num)
    length = lenNum/2
    for i in range(length):
        if num[i] != num[lenNum - 1]:
            return False
        
    return True    
    
    
FairandSquare()    
    
    
        
        

        
        
        
        
        