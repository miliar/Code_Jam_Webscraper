from datetime import datetime
import copy
 
#Input
#fName = input('Enter Filename of Input:\n')
with open('test.in') as f:
    inp = [line.rstrip() for line in f]
#Output
proj = 'standing '
timestamp = datetime.now().strftime("%H.%M.%S")
out = open(proj+timestamp+'.out', 'w')
 
#Stuff
caseCount = int(inp[0])

for case in range(1,caseCount+1):
    print(case)
    lineNo = case
    line = inp[lineNo].split()
    maxShy = int(line[0])
    shynesses = [int(i) for i in line[1]]

    standing = 0
    addFreinds = 0

    for x in range(0, maxShy+1):
        shyLevel = shynesses[x]
        diff = x - standing - addFreinds
        if shyLevel > 0 and diff > 0:
            addFreinds += diff
        standing += shyLevel
    
    out.write('Case #%d: %d\n'%(case,addFreinds))
out.close()
