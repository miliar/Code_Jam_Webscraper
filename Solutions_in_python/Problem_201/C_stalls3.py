#!/usr/bin/python3
# Python version >= 3.6

import heapq

def split(span):
    d, m = divmod(span-1,2)
    return (d+m, d)

def find_stall(N,K):
    stack = [-N]
    tocheck = {N:1}
    k = K
    while k > 0:
        span = -heapq.heappop(stack)
        if span == 1:
            return (0,0)
        sp = split(span)
        num = tocheck.pop(span)
        for z in sp:
            
            if z in tocheck:
                tocheck[z] += num
            else:
                tocheck[z] = num
                heapq.heappush(stack, -z)
        k -= num

    return sp





if __name__=="__main__":
    T = int(input())

    for case in range(T):
        print(f"Case #{case+1}: ", end="")

        N, K = (int(x) for x in input().split())
        L, R = find_stall(N,K)
        print(f"{L} {R}")
        

