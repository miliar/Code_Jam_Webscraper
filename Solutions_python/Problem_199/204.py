from math import ceil

def compute(pattern, K):
    c = 0
    for i in range(len(pattern)-K+1):
        if pattern[i] == False:
            c += 1
            for j in range(i,i+K):
                pattern[j] = not pattern[j]

    for i in range(len(pattern)-K+1, len(pattern)):
        if pattern[i] == False:
            return "IMPOSSIBLE"
    return c
            
                                    
T = int(input())
for t in range(1,T+1):
    s, k = input().split()
    s = [x == '+' for x in s]
    k = int(k)

    print("Case #%d: "%t, compute(s,k)) 
