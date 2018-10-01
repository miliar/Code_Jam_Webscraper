def helper():
    input = raw_input()
    S, K = input.strip().split()
    K = int(K)
    
    #print(S, K)

    s = [0 if S[i] == '-' else 1 for i in range(len(S))] 

    #print(s, K)
    if sum(s) == len(s): return 0
    
    if len(s) == K and sum(s) == 0: return 1
    
    if len(s) <= K and sum(s) != len(s):
        return "IMPOSSIBLE"

    count = 0

    for i in range(len(s) - K + 1):
        if s[i] == 0:
            s = flip(s, i, K)
            count += 1 

    # print(s)        
    if sum(s) < len(s):
        return "IMPOSSIBLE"
    else:
        return count
            
            
def flip(s, i, K):
    for j in range(K):
        s[i + j] = 1 if s[i + j] == 0 else 0
    # print(s)    
    return s

                
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, helper())