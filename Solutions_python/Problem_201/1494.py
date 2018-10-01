def make_choice(N):
    R = N/2
    L = N/2 if N%2 else N/2-1
    return max(L,R), min(L,R)
    
    
def solve(N, K):
    if N==K: return (0,0)
    if K==1: return make_choice(N)
    if K==0: return None
    
    N_R = N/2
    N_L = N/2 if N%2 else N/2-1
    
    K -= 1 #one persone will occupy one stall. Others need to be distributed
    K_L = K/2
    K_R = K/2+1 if K%2 else K/2
    
    choice_L = solve(N_L, K_L)
    choice_R = solve(N_R, K_R)
    
    return choice_L if choice_R == None else ( choice_R if choice_L == None else min(choice_L, choice_R) )

t = int(raw_input())
for i in xrange(1, t+1):
    N, K = [ int(j) for j in raw_input().split(" ") ]
    print "Case #{}: {} {}".format(i, *solve(N, K))