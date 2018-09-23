from math import pi
from itertools import combinations


def prints(s, x):
    print("Case #{}: {}".format(s, function(x)))

def function(com):
    ans = 0
    for i in com:
        big = 0
        ch = 0
        h = 0
        for x in i:
            if x[0] > big:
                 big = x[0]
            ch = ch + (2*pi*x[0]*x[1])

        for x in i:
            h = h + x[1]
        if (pi*(big**2) + ch) > ans:
            ans = (pi*(big**2) + ch)
    return ans

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    cake = []
    for _ in range(n):
        cake.append(list(map(int, input().split())))
    comb = list(map(list, combinations(cake, k)))
    prints(t, comb)



