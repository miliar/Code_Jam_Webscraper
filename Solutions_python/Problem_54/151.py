import sys

def euclid(numA, numB):
    while numB != 0:
        numRem = numA % numB
        numA = numB
        numB = numRem
    return numA

C = int(sys.stdin.readline())
for c in range(1, C+1):
    N,t = sys.stdin.readline().split(None, 1)
    ti = map(int, t.split())
    m = min(ti)
    for i in range(len(ti)):
        ti[i] -= m
    g = ti[0]
    for i in range(1,len(ti)):
        g = euclid(g, ti[i])
    m %= g
    if(0 == m):
        g = 0
    else:
        g -= m
    print "Case #"+str(c)+": "+str(g)
