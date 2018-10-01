#!/usr/bin/env python 
def solve(S,K):
    K=int(K)
    l=[True]*len(S)
    for i in range(len(S)):
        l[i]=S[i]=='+'
    count=0
    for i in range(len(l)):
        if not l[i]:
            if i>len(l)-K:
                return "IMPOSSIBLE"
            for i in range(i,i+K):
                l[i]=not l[i] 
            count+=1
    return count

t = int(raw_input())
for cas in xrange(1,t+1):
    ans = solve(*raw_input().split())
    print "Case #{}: {}".format(cas,ans)
