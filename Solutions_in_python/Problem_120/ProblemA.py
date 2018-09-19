'''
Created on Apr 27, 2013

@author: DELL LATITUDE E4300
'''
import math
def startReadingInput():
    f = open("A-small-attempt0.in")
    T = int(f.readline())
    for i in range(T):
        cost = solve(f)
        
        print 'Case #{0}: {1}'.format(i + 1, cost)
        
            
            
            
def solve(f):
    drawingCost = 0
    rtStr = f.readline().split()
    r, t = map(int, rtStr)
    
   
    outer = 0
    inner = 0
    countB = 0
    countW = 0
   
    while drawingCost <= t:
        countB += 1
        outer = (r + countB + countW)**2
        inner = (r + countB + countW - 1)**2
        countW += 1
        drawingCost = drawingCost + outer - inner
    
    
    radiusRequired = math.floor((math.sqrt(t)))
    
#    countW = countB + 1
#    while drawingCost > t:
#        outer = (r + countB + countW)**2
#        inner = (r + countB + countW - 1)**2
#        drawingCost = drawingCost + outer - inner
#        
      
#    print 'Radius: ' + str(radiusRequired)
#    countW_countB = radiusRequired - r
#    total = 0
#    while total <= countW_countB:
#        countW += 1
#        total = 2*countW + 1
#        
#    
#    if 2*countW == countW_countB:
#        countB = countB - 1
#        
#    countB = countW + 1 + countB
#    print 'B: ' + str(countB)
#    print 'W: ' + str(countW)
    countB = countB - 1
    return countB
    
startReadingInput()  