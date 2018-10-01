import sys

def combin(P,u,k):
    if K==1:
        P = sorted(P,key=lambda x:-x)
        k = 0
        while u>0:
            g = (1-P[k])
            s = min(g,u)
            P[k]+=s
            if abs(1-P[k])<1e-6:
                k+=1
            u-=s
        res = 1
        for p in P:
            res*=(1-p)
        return 1-res
    res = 1
    for p in P:
        res*=p
    return 0

def simple(P,u):
    P = sorted(P)
    ps = 0
    pt = P[0]
    stop = 1
    for i in range(1,len(P)):
        ps+=(P[i]-pt)*i
        if ps>u:
            break
        stop = i+1
        pt = P[i]
    used = 0
    for j in range(stop-1):
        used += (P[stop-1]-P[j])
        P[j]=P[stop-1]
    l = u-used
    lk = l/stop
    for j in range(stop):
        P[j]+=lk
    res = 1
    for p in P:
        res*=p
    return res

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    line = [int(x) for x in input().split()]
    N,K = line[0],line[1]
    U = float(input())
    P = [float(x) for x in input().split()]
    res = simple(P,U) if N==K else combin(P,U,K)
    print("Case #{}: {}".format(i, res))
    # print(i, file=sys.stderr) #DEBUG
