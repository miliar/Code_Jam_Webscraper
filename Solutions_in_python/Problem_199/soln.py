#!/usr/bin/python

def doIt(s,k):
    j=0
    n=len(s)
    cnt = 0
    while j < n:
        while j < n and s[j] != '-':
            j+=1

        if j >= n:
            continue
        if s[j] == '-' and j > (n-k):
            return 'IMPOSSIBLE'

        if s[j] == '-':
            for l in range(j,j+k):
                s[l] = '+' if s[l] == '-' else '-'
            cnt += 1
        j+=1
    return cnt



nt=int(raw_input())
for i in range(1, nt+1):
    s,k=raw_input().split()
    s=list(s)
    k=int(k)
    #print s,k
    ans=doIt(s,k)
    print "Case #{}: {}".format(i,ans)
    
