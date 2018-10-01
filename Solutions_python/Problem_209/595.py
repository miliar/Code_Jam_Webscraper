import math, heapq
from decimal import *
t = int(input())
for i in range(1, t + 1):
    N, K = [int(s) for s in input().split(" ")]
    pancakes = []
    for n in range(N):
        R, H = [int(s) for s in input().split(" ")]
        outer_sa = Decimal(math.pi) * Decimal(R) * Decimal(2) * Decimal(H)
        top_sa = Decimal(math.pi) * Decimal(R) ** Decimal(2)
        sa = outer_sa + top_sa
        #print("Surface Area of this Pancake is {}".format(sa))
        pancakes.append([sa, outer_sa, top_sa])
    #print(pancakes)
    pancakes.sort(key=lambda x: x[2], reverse=True)
    #print(pancakes)
    max_ea = -1
    for base in range(len(pancakes)):
        ea = pancakes[base][0] + sum(num[1] for num in \
        heapq.nlargest(K-1, pancakes[base+1:], key=lambda x: x[1]))
        if ea > max_ea:
            max_ea = ea
    #print("=============================================\n")
    print("Case #{}: {}".format(i, max_ea));
    #print("=============================================\n")
