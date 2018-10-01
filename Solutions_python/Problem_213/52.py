#!/usr/bin/env python3

# Google Code Jam Round 2 2017
# Problem B. Roller Coaster Scheduling
# Solution in Python 3
# By Smithers

for x in range(1, int(input()) + 1):
    n, c, m = map(int, input().split())
    tickets = [list(map(int, input().split())) for i in range(m)]
    
    t = [[0] * n, [0] * n]
    for p, b in tickets:
        t[b-1][p-1] += 1
    
    y = max(sum(t[0]), sum(t[1]))
    a = 0
    for i in range(n):
        a += t[0][i] + t[1][i]
        y = max(y, (a + i) // (i + 1))
    z = 0
    for i in range(n):
        a = t[0][i] + t[1][i]
        z = max(z, a - y)
    
    print('Case #{}: {} {}'.format(x, y, z))
