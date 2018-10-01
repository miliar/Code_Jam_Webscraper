##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(s):
    
    n = [int(item) for item in s]

    for i in range(len(n)-1):
        # check for subsequent digits in decreasing order
        if n[i+1]<n[i]:
            n[i] -= 1

            # carry to higher digits
            while i>0 and n[i]<n[i-1]:
                i -= 1
                n[i] -= 1

            # fill up with 9 and abort
            for j in range(i+1,len(n)):
                n[j] = 9
            break

    return "".join([str(item) for item in n]).lstrip('0')
    
    
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    s = input().rstrip()
        
    ## solve and print result
    result = solve(s)
    print('Case #'+str(t+1)+': '+str(result))

    
