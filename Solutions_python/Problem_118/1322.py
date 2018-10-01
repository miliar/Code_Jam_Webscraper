

# -*- coding: utf-8 -*-

import math
def is_perfect_square(n):
    res       = math.sqrt(n)
    intNumber = math.trunc(res)
    return res == intNumber, intNumber
                        
                                                  
def jobRun(start, end):
    ''' Fair and Square numbers in [start, end]
    '''
    counter = 0
    for i in xrange(start, end+1):
        s = str(i)
        if s == s[::-1]:
            if is_perfect_square(i)[0]:
                s2 =str(is_perfect_square(i)[1])
                if s2 == s2[::-1]:
                    counter +=1
    return counter
                    
                
            
    

        

def getinput():
    file = r'C:\ewy\C-small-attempt0.in'
    return open(file, 'r')

def saveoutput(results):
    resFile = r'C:\ewy\C-small.out'
    with open(resFile, 'w') as f:
        f.writelines(results)



def main():

    f = getinput()
    with f:
        N = int(f.readline())
        print 'N:', N
        
        resLines = ''
        for case in range(1,N+1):
            
            [start, end] = f.readline().strip().split()
            start, end = int(start), int(end)
            
            res = jobRun(start, end)
        
            resLine = 'Case #{case}: {res}'.format(case=case, res=res)
            print resLine
            resLines +=resLine + '\n'
            
    saveoutput(resLines)