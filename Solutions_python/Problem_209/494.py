from sys import stdin
import math

Pi=math.pi

def areaLat(pancake):
    (radius,height)=pancake
    return (2*Pi*radius*height)

def partialAns(first,pancakes):
    L=pancakes[first+1:]
    L.sort(key=areaLat,reverse=True)
    LL=L[0:K-1]
    a = Pi*pancakes[first][0]**2 + areaLat(pancakes[first])
    for p in LL:
        a+=areaLat(p)
    return a


def answer(K,pancakes):
    pancakes.sort(reverse=True)
    r=partialAns(0,pancakes)
    for i in range(1,N):
        a = partialAns(i,pancakes)
        if a>r:
            r=a
    return str(r)



T=int(stdin.readline())
for case in range(1,T+1):
    c = stdin.readline().split()
    [N,K]=list(map(int,c))
    pancakes=[]
    for i in range(N):
        [r,h] = list(map(int,stdin.readline().split()))
        pancakes.append((r,h))
    print('Case #%i: %s' % (case,answer(K,pancakes)))


