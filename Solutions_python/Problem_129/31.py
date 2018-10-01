#!/usr/bin/python3

import sys
MOD = 1000002013

T = int(sys.stdin.readline())
caseNum = 0

def priceToPay(a, b, p, N):
    d = b - a
    oneTicket = (d * N - d*(d-1)//2) % MOD
    return (p * oneTicket) % MOD

def solve(N, data):
    events = []
    shouldPay = 0
    for o, e, p in data:
        shouldPay += priceToPay(o, e, p, N)
        shouldPay %= MOD
        events.append( (o, 0, p) )
        events.append( (e, 1, p) )
    events.sort()
    
    stack = []
    actPaid = 0
    for x, t, p in events:
        if t == 0:
            # p people entered at x
            stack.append( [x, p] )
        else:
            # p people go out at x
            while len(stack) > 0 and stack[-1][1] <= p:
                actPaid += priceToPay(stack[-1][0], x, stack[-1][1], N)
                actPaid %= MOD
                p -= stack[-1][1]
                stack.pop()
            if p > 0:
                stack[-1][1] -= p
                actPaid += priceToPay(stack[-1][0], x, p, N)
                actPaid %= MOD
    return (shouldPay - actPaid) % MOD

while caseNum < T:
    caseNum += 1
    N, M = map(int, sys.stdin.readline().strip().split(' '))
    data = [tuple(map(int, sys.stdin.readline().strip().split(' '))) for i in range(M)]
    print("Case #{0}: {1}".format(caseNum, solve(N, data)))
