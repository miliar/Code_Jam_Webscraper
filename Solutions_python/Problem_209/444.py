import math as mt
t = int(input())
for i in range(1, t+1):
    n,k = [int(x) for x in input().split(' ')]
    side = []
    rcol = []
    col = []
    max_r = 0
    for j in range(n):
        r,h = [int(x) for x in input().split(' ')]
        col.append([r,h])
    col.sort()
    side = [2*mt.pi*x[0]*x[1] for x in col]
    circle = [mt.pi*x[0]**2 for x in col]
    if k != 1:
        choose = side[:k]
        max_cir = circle[k-1]
        for a in range(k,n):
            if circle[a] - circle[a-1] + side[a] > min(choose):
                choose.remove(min(choose))
                choose += [side[a]]
                max_cir = circle[a]
        area = sum(choose) + max_cir
    else:
        mix = [side[a]+circle[a] for a in range(n)]
        area = max(mix)
    print("Case #{}: {}".format(i,area))
