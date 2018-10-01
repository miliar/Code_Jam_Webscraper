import numpy as np

t = int(raw_input())

for z in range(1,t+1):

    d,n = map(int, raw_input().split(' '))

    a = []

    for _ in range(n):
        x,y = map(float, raw_input().split(' '))
        a.append((d-x)/y)

    ans = d/max(a)

    print "Case #%d: %f" %(z,ans)

