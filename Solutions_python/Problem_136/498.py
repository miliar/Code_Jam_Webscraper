##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(c,f,x):
    # number of farms to be considered
    n = int(x/c)+1

    # time for no farm
    t = x/2
    t0 = c/2
    
    for i in range(1,n):
        # check whether buying i farms is better
        t = min(t,x/(2+i*f)+t0)
        t0 += c/(2+i*f)
        
    return "%.7f" % t
    
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    [c,f,x] = [float(item) for item in input().rstrip().split()]
        
    ## solve and print result
    result = solve(c,f,x)
    print('Case #'+str(t+1)+': '+str(result))
