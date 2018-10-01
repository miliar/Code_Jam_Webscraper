import string
import heapq
from heapq import heappush, heappop

def sol(numStalls, numPeople):
    numBlocks = {numStalls: 1} #for each block size, keep track of how much there are
    while True:
        curr = max(numBlocks)
        if numBlocks[curr] >= numPeople:
            break
        numPeople -= numBlocks[curr]
        
        if curr % 2 == 1:
            if int((curr-1)/2) in numBlocks:
                numBlocks[int((curr-1)/2)] += 2*numBlocks[curr]
            else:
                numBlocks[int((curr-1)/2)] = 2*numBlocks[curr]
        else:
            if int(curr/2) in numBlocks:
                numBlocks[int(curr/2)] += numBlocks[curr]
            else:
                numBlocks[int(curr/2)] = numBlocks[curr]
            if int(curr/2)-1 in numBlocks:
                numBlocks[int(curr/2)-1] += numBlocks[curr]
            else:
                numBlocks[int(curr/2)-1] = numBlocks[curr]

        del numBlocks[curr]
    

    
    if curr % 2 == 1:
        mymin = (curr-1)/2
        mymax = (curr-1)/2
    else:
        mymin = curr/2 - 1
        mymax = curr/2
        
    

    return str(int(mymax))+" "+str(int(mymin))


fIn = open('input.in', 'r')
fOut = open('output.txt', 'w')
case = 0
for line in fIn:
    print(case)
    if case > 0:
        n = int(line.split()[0])
        k = int(line.split()[1])
        fOut.write("Case #"+str(case)+": "+str(sol(n,k))+"\n")
    case += 1