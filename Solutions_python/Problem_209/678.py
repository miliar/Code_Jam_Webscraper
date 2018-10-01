from math import pi
T = int(input())
class pancake:
    def __init__(self, r, h):
        self.r = r
        self.h = h

for case in range(1,T+1):
    n,k=tuple(map(int,list(input().split())))

    pancakes=[]
    a = []
    for i in range(0, n+1):
        a.append([])
        for j in range(0, k+1):
            a[i].append(0)
    for i in range(1, n + 1):
        rx,hx = tuple(map(int,list(input().split())))
        pancakes.append(pancake(rx,hx))
    pancakes.sort(key=lambda x: x.r, reverse=True)
    area = float(0)
    for i in range(0, n):
        a[i][0] = pi * pancakes[i].r*pancakes[i].r+ 2* pi*pancakes[i].r*pancakes[i].h
        if a[i][0] > area:
            area = a[i][0]

    for j in range(1, k):
        for i in range(j, n):
            #print(i, j)
            a[i][j] = 2*pi*pancakes[i].r*pancakes[i].h+ a[0][j-1]
            if a[i][j] > area:
                area = a[i][j]
            for k in range(1, i):
                if 2*pi*pancakes[i].r*pancakes[i].h + a[k][j-1] > a[i][j]:
                    a[i][j] = 2*pi*pancakes[i].r*pancakes[i].h + a[k][j-1]
                    if a[i][j] > area:
                        area = a[i][j]
                #print(i,j,k)


    print("Case #{}: {:.9f}".format(case, area))