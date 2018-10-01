import sys
import math



count = 1
for line in sys.stdin.readlines()[2::2]:
    entries = line.strip().split(' ')
    
    candy =[int(x) for x in entries]
    
    candy.sort()

    #print candy

    best = -1
    for i in range(1, len(candy)):
        sean = candy[i:]
        pat = candy[:i]

        pSean = reduce(lambda x,y: x^y, sean)
        pPat = reduce(lambda x,y: x^y, pat)

        sSean = reduce(lambda x,y: x+y, sean)
        sPat = reduce(lambda x,y: x+y, pat)

        #print pSean, pPat
        #print sSean, sPat
        #print best

        if pSean == pPat and sSean > best:
            best = sSean

    if best == -1:
        best = "NO"
    else:
        best = str(best)

    print "Case #" + str(count) + ": " + best
    count += 1 
