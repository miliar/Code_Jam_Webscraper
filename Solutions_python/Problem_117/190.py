def solve(N,M,a):
    ## determine lawnmower settings
    rowH = [max(a[row]) for row in range(N)]
    colH = [max([a[row][col] for row in range(N)]) for col in range(M)]

    ## check squares
    for row in range(N):
        for col in range(M):
            if a[row][col]<min(rowH[row],colH[col]):
                return 'NO'

    return 'YES'
                    
##            
## MAIN PROGRAMM
##
T = int(input())
for t in range(T):
    ## read case
    N,M = map(int, input().rstrip().split())
    a = [list(map(int, input().rstrip().split())) for _ in range(N)]
        
    ## solve and print results
    result = solve(N,M,a)
    print('Case #'+str(t+1)+': '+str(result))


    
