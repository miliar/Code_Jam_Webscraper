#!/usr/bin/env python
"""
    I used this to pre-compute the palisq:
    
    def pali(what):
        x = str(what)
        return x == x[::-1]
    
    i = 1
    palis = []
    palisq = []
    while i*i <= 10**14:
        if (pali(i)):
            palis.append(i)
        i+=1
    for t in palis:
        if (pali(t*t)):
            palisq.append(t*t)

    print(palisq)

    it ran in 18 seconds :)
       
"""

palisq = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]

n = int(input())
for I in range(1, n+1):
    x, y = [int(t) for t in input().split()]
    res = 0
    for v in palisq:
        if (v >= x and v <= y):
            res += 1
    print("Case #" + str(I) + ": " + str(res))

