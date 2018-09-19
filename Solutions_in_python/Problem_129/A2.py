import sys
    
def solve(N,M,jList):
    ## compute passenger in out and ticket costs
    cost = 0
    eList = dict()
    oList = dict()
    sList = set()
    for o,e,p in jList:
        sList.add(o)
        sList.add(e)
        cost += p*((e-o)*N - (e-o)*(e-o-1)//2)
        if o in oList:
            oList[o] += p
        else:
            oList[o] = p
        if e in eList:
            eList[e] += p
        else:
            eList[e] = p

    sList = list(sList)
    sList.sort()
    
    ## simulate train travel
    lastS = 1
    tStack = []
    payed = 0
    for s in sList:
        
        ## entering passengers
        if s in oList:
            tStack.append([s,oList[s]])

        ## leaving passengers
        if s in eList:
            ## get rid of latest tickets
            p = eList[s]
            while p>0:
                if tStack[-1][1]<=p:
                    so,l = tStack.pop(-1)
                    p -= l
                else:
                    so = tStack[-1][0]
                    tStack[-1][1] -= p
                    l = p
                    p = 0
    
                payed += l*((s-so)*N - (s-so)*(s-so-1)//2)
        
    return (cost-payed) % 1000002013
                    
##            
## MAIN PROGRAM
##
T = int(input())
for t in range(T):
    ## read case
    N,M = map(int, input().rstrip().split())
    jList = [list(map(int, input().rstrip().split())) for _ in range(M)]
        
    ## solve and print results
    result = solve(N,M,jList)
    print('Case #'+str(t+1)+': '+str(result))

    ##progress output
    print('Done: '+str(t+1)+' of '+str(T), file=sys.stderr)

    
