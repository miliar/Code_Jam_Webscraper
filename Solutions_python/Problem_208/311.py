from collections import defaultdict
from heapq import *

def dijkstra(g, es, f, t):
    
    q, seen = [(0.,f,es[f])], set()
    
    mintime = float("inf")
    
    while q:
        (cost,v1,ee) = heappop(q)
#        if v1 not in seen:
        if 1==1:
            seen.add(v1)
            
            if v1 == t: mintime = min(cost, mintime)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    
                    if es[v1][0]>=c and ee[0]>=c:
                        if es[v1][0]>=ee[0] and es[v1][1]>=ee[1]:
                            heappush(q, (cost+c/es[v1][1], v2, (es[v1][0]-c, es[v1][1])))
                        elif es[v1][0]<=ee[0] and es[v1][1]<=ee[1]:
                            heappush(q, (cost+c/ee[1], v2, (ee[0]-c, ee[1])))
                        else:
                            heappush(q, (cost+c/es[v1][1], v2, (es[v1][0]-c, es[v1][1])))
                            heappush(q, (cost+c/ee[1], v2, (ee[0]-c, ee[1])))
                    elif es[v1][0]>=c:
                        heappush(q, (cost+c/es[v1][1], v2, (es[v1][0]-c, es[v1][1])))
                    elif ee[0]>=c:
                        heappush(q, (cost+c/ee[1], v2, (ee[0]-c, ee[1])))
    return mintime

t = int(raw_input())  # read a line with a single integer
for tt in xrange(1, t + 1):
    
    N, Q = [int(s) for s in raw_input().split(" ")]
    
    es = []
    for k in xrange(N):
        es.append([float(s) for s in raw_input().split(" ")])
    
    g = defaultdict(list)
    for k in xrange(N):
        curr = [float(s) for s in raw_input().split(" ")]
        g[k] = [(curr[i], i) for i in xrange(N) if curr[i]>0]
    
    out = "Case #{}: ".format(tt)
    
    #print out
    #print N, Q
    #print es
    #print g
    
    for kk in xrange(Q):
        init, final = [int(s)-1 for s in raw_input().split(" ")]
        aa = dijkstra(g, es, init, final)
        #print init, final
        out += "{0:.8f} ".format(aa)

    print out