import os
import time

t1 = time.clock()

inHandle = open('A-small-attempt2.in','r')
outHandle = open('output.txt','w')

nCases = int(inHandle.readline().replace('\n',''))
use = [1,0,2,3,4,5,6,7,8,9]

for case in range(nCases):
    message = inHandle.readline().replace('\n','')
    s = len(message)
    number = ''
    seen = []
    used = -1
    for x in range(s):
        workingWith = message[x]
        if(workingWith not in seen):
            seen.append(workingWith)
            used = used + 1
            number = number + str(use[used])
        else:
            number = number + str(use[seen.index(workingWith)])

    base = int(max(number)) + 1

    answer = 0
    for j in range(s):
        digit = number[s-j-1]
        answer = answer + pow(base, j) * int(digit)
        
            
    outHandle.write('Case #' + str(case+1) + ': ' + str(answer) + '\n')

inHandle.close()
outHandle.close()

t2 = time.clock()
print 'total time taken to execute = ' + str(t2-t1)
