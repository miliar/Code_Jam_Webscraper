'''
Created on 14/04/2012

@author: michael
'''
def count_pairs(a,b):
    pairs = 0
    distinct_checker = set()
    for n in xrange(a,b+1):
        n = str(n)
        for i in xrange(1,len(n)):
            m = int(n[i:]+n[:i])
            if (int(n), m) in distinct_checker:
                continue
            else:
                distinct_checker.add( (int(n), m) )
            if a <= int(n) < m <= b:
                pairs += 1
    return str(pairs)

inFile = open('C-small-attempt0.in','r')
outFile = open('C-small-attempt0.out','w')

noCases = int(inFile.readline().strip())

for i in range(noCases):
    inp = inFile.readline().strip().split(' ')
    if i < noCases - 1:
        outFile.write('Case #'+ str(i+1) +': ' + count_pairs(int(inp[0]), int(inp[1])) + '\n') 
    else:
        outFile.write('Case #'+ str(i+1) +': ' + count_pairs(int(inp[0]), int(inp[1])))
inFile.close()
outFile.close()