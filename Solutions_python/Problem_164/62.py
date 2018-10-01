import sys

##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(n,l):
    hList = []
    for d,h,m in l:
        for i in range(h):
            hList.append((d,m+i))
            
    ## one hiker no problem
    if len(hList)<2:
        return 0

    assert(len(hList)==2)
    
    ## two hikers sorted
    (d1,m1) = hList[0]
    (d2,m2) = hList[1]
    if d2<d1:
        (d1,m1) = hList[1]
        (d2,m2) = hList[0]

    if m1==m2:
        return 0

    if m2>m1:
        return int(m2*(360-d2) >= m1*(720-d1))
    else:
        return int(m1*(360-d1) >= m2*(720-d2))
    
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    n = int(input())
    l = [[int(item) for item in input().rstrip().split()] for _ in range(n)]
        
    ## solve and print result
    result = solve(n,l)
    print('Case #'+str(t+1)+': '+str(result))

    ## progress output
    print('Done: '+str(t+1)+' of '+str(T), file=sys.stderr)
