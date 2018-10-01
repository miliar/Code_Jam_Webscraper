
from bisect import bisect_right,bisect_left
inFile = open("D-large.in")
outFile = open("D-large.out","w")

T = inFile.readline()
T = int(T)

for num in range(0,T):
    N = int(inFile.readline())
    
    line = inFile.readline()
    blocksN = line.split(" ");
    blocksN = [float(x) for x in blocksN]
    blocksN.sort()
    tBlocksN = list(blocksN)
    
    #print(blocksN)
    line = inFile.readline()
    blocksK = line.split(" ");
    blocksK = [float(x) for x in blocksK]
    blocksK.sort()
    tBlocksK = list(blocksK)
    #print(blocksK)
    
    countN = 0
    countD = 0
     
    for i in range(0,N):
        #if (blocksN[i] > blocksK[N-i-1]):
#   countD += 1
        if ( tBlocksN[0] < tBlocksK[0]):
            del tBlocksN[0]
            del tBlocksK[N-i-1]     
        else:
            k = bisect_left(tBlocksK,tBlocksN[0])    
            del tBlocksK[k-1]
            del tBlocksN[0]
            countD += 1
            
    tBlocksK = list(blocksK)
    tBlocksN = list(blocksN)
    for i in range(0,N):
        if ( tBlocksN[N-i-1] > tBlocksK[N-i-1]):
            del tBlocksN[N-i-1]
            del tBlocksK[0]     
            countN += 1
        else:
            k = bisect_right(tBlocksK,tBlocksN[N-i-1])    
            del tBlocksK[k]
            del tBlocksN[N-i-1]
    print (str(countN))
    print (str(countD))                
    
    outFile.write("Case #"+str(num+1)+": "+str(countD)+" "+str(countN)+"\n")

inFile.close();
outFile.close();