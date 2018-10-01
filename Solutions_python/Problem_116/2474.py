'''
Created on Apr 13, 2013

@author: matthias
'''

import scipy as s
import timeit

from q01_LargeInput import *

def findT(inMatrix):
    for i in range(inMatrix.size):
        Tidx=inMatrix[i].find('T')
        if Tidx>=0:
            return (i, Tidx)

def checkWon(inX, inChar):
    X = inX.copy()
    #    http://stackoverflow.com/questions/432112/python-numpy-array-help-is-there-a-function-to-return-the-index-of-something
    X[s.where(X=='T')]=inChar
    cmpvec = s.array( list(inChar*4) )
    for i in range(X.shape[0]):
        if(s.all(X[i,:] == cmpvec)): #won in row
            return True
        if(s.all(X[:,i] == cmpvec)): #won in column
            return True
        
    diag1=s.array([X[i,i] for i in range(X.shape[0])])
    diag2=s.array([X[i,-i-1] for i in range(X.shape[0])])
    if(s.all(diag1 == cmpvec) or s.all(diag2 == cmpvec)):
        return True
    return False

def isGameOver(inX):
    return not s.any(inX=='.')
    
def checkSubGame(M):
    if(checkWon(M,'O')):
        return 'O won'
    if(checkWon(M, 'X')):
        return 'X won'
    if(isGameOver(M)):
        return "Draw"
    return "Game has not completed"
    
    
        
def resultString(inString):
    sout=""
    stringList = inString.split('\n')
    
    N = int( stringList.pop(0) )
    for n in range(N):
        sout+= "Case #" + str(n+1) + ": "
        toA = []
        for i in range(4):
            toA.append(stringList.pop(0))
        #remove empty line
        stringList.pop(0)
    
        A = s.array([list(row) for row in toA])    
        sout+= checkSubGame(A)
        sout+= "\n"
        
    return sout
    
    
    
if __name__ == '__main__':
#    print timeit.timeit('resultString(sInput)',
#                  "from __main__ import *", number=10)
    sRes = resultString(sInput)
    with open('q01_res.txt', 'w') as f:
        f.write(sRes)
