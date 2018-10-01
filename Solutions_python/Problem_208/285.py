import sys
from collections import defaultdict
from heapq import *

def aStartNavigate(s,e,hs,d):
    pass

def dijkstra(s,e,hs,d):
    g = defaultdict(list)
    for i in range(len(d)):
        for j in range(len(d)):
            if (i!=j) and (d[i][j]!=-1):
                g[i].append((d[i][j],j))
    q = [(0,(s,0,0),(),set())]
    while q:
        (cost,v1,path,pSeen) = heappop(q)
        path = (v1[0],path)
        if v1[0]==e: return (cost,path)
        for c, v2 in g.get(v1[0], ()):
            if c<=v1[1]:
                heappush(q, (cost+(c*1.0/v1[2]), (v2,v1[1]-c,v1[2]), path, seen))
            if v1[0] not in pSeen:
                seen = set(pSeen)
                seen.add(v1[0])
                heappush(q, (cost+(c*1.0/hs[v1[0]][1]), (v2,hs[v1[0]][0]-c,hs[v1[0]][1]), path, seen))
    return (float("inf"),0,0,0)


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    line = input().split()
    n = int(line[0])
    q = int(line[1])
    horses = []
    for j in range(n):
        horses.append([int(x) for x in input().split()])
    d = []
    possibilities = [[0,0,0]]
    for j in range(n):
        d.append([int(x) for x in input().split()])
        newPos = []
        if (j<n-1):
            for pHorse in possibilities:
                if pHorse[0]>d[j][j+1]:
                    newPos.append([pHorse[0]-d[j][j+1],pHorse[1],pHorse[2]+d[j][j+1]/float(pHorse[1])])
                if horses[j][0]-d[j][j+1]>=0:
                    newPos.append([horses[j][0]-d[j][j+1],horses[j][1],pHorse[2]+d[j][j+1]/float(horses[j][1])])
            possibilities = newPos
    possible = len(possibilities)>0
    if possible:
        res = min(possibilities,key=lambda x:x[2])[2]
    else:
        res=-1
    res=res if possible else -1
    routes = []
    res = []
    for j in range(q):
        routes.append([int(x) for x in input().split()])
        res.append(dijkstra(routes[j][0]-1,routes[j][1]-1,horses,d)[0])


    print("Case #{}: {}".format(i, " ".join([str(x) for x in res])))
    # print(i, file=sys.stderr) #DEBUG
