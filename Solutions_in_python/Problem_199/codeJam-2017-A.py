T = int(raw_input().strip())
for i in range(T):
    temp = map(str, raw_input().strip().split(" "))
    S = temp[0]
    K = int(temp[1])
    n = len(S)
    pancakes = []
    for j in range(n):
        if S[j] == "-": pancakes.append(0)
        else: pancakes.append(1)
    #print S, pancakes
    
    answer = 0
    for j in range(n-K+1):
        if pancakes[j] == 0:
            answer += 1
            for k in range(j,j+K):
                if pancakes[k] == 0: pancakes[k] = 1
                else: pancakes[k] = 0
    for j in range(n-K+1,n):
        if pancakes[j] == 0:
            answer = "IMPOSSIBLE"
            
    print "case #" + str(i+1) + ": " + str(answer)
            
            
    