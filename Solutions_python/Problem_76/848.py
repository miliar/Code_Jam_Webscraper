f = open('C-small-attempt1.in','r')
out = open('smalloutput.txt','w')

numlines = int(f.readline())

for i in range(numlines):
    out.write('Case #%d: ' % (i+1))
    numCandies = int(f.readline())
    line = f.readline()
    
    values = map(lambda x: int(x), line.split(' '))
    
    if(len(values) != numCandies):
        print 'Bad input!'
        break
    
    numSubsets = 2**(len(values))
    
    found = False
    
    maxval = 0
    
    # For each possible subset
    for subset in range(1,numSubsets-1):
        
        trueSumA = 0
        trueSumB = 0
        xorSumA = 0
        xorSumB = 0
        
        # Calculate the true sum and the xor sum
        for v in range(len(values)):
            if(subset & (1 << v) != 0):
                xorSumA ^= values[v]
                trueSumA += values[v]
            else:
                xorSumB ^= values[v]
                trueSumB += values[v]
            
        if(xorSumA == xorSumB):
            if(max(trueSumA,trueSumB) > maxval):
                maxval = max(trueSumA,trueSumB)    
            found = True

    if(not found):
        out.write('NO\n')
        print 'NO'
    else:
        out.write('%d\n' % maxval)
        print maxval

out.close()
f.close()