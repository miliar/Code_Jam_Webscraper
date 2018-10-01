import psyco
psyco.full()
from math import *
inn = open('input.txt', 'r')
def getz():
    global inn
    return inn.readline().strip()
def geiz():
    return int(getz())
def gelz():
    return map(int,getz().split())
T = int(getz())

def area(x1,x2,x3,y1,y2,y3):
    return abs( (x1-x2)*(y1-y3) - (y1-y2)*(x1-x3) )

def primes(n):
    if n < 2: return []
    if n == 2: return [2]
    s = range(3, n, 2)
    mroot = n ** 0.5
    half = len(s)
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3)//2
            s[j] = 0
        while j < half:
            s[j] = 0
            j += m
        i = i + 1
        m = 2 * i + 3
    return [2]+[x for x in s if x]

def go(n,m,a):
    for i in range(n+1):
        for j in range(n+1):
            for h in range(m+1):
                for y in range(m+1):
                    if abs(i*y-j*h) == a:
                        return 0,0,i,h,j,y
plt = primes(10000)
global plt
for tc in range(T):
    n,m,a = gelz()
    #find i j  <= n and h,y <= m with |iy-jh| = a
    z = go(n,m,a)
    if z == None:
        print "%s%d%s%s" % ( "Case #",tc+1,": ","IMPOSSIBLE" )
    else:
        print "%s%d%s%d%s%d%s%d%s%d%s%d%s%d" % ( "Case #",tc+1,": ",z[0]," ",z[1],
                                       " ",z[2]," ",z[3]," ",z[4]," ",z[5])

