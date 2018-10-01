##            
## PROBLEM SOLVING ALGORITHM 
##
def solve(s,k):
    res = 0
    s = [item=='+' for item in s]

    # just test by starting from one side
    for i in range(len(s)-k+1):
        if not s[i]:
            res += 1
            for j in range(k):
                s[i+j] = not s[i+j]
    if False in s:
        return "IMPOSSIBLE"
    return res
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    s,k = input().rstrip().split()
        
    ## solve and print result
    result = solve(s,int(k))
    print('Case #'+str(t+1)+': '+str(result))

