import sys
import time
import math
from collections import defaultdict

def read(f = int): return f(input())
def readlist(f = int): return list(map(f, input().split()))
def printd(msg): print(msg); print(msg, file=sys.stderr)

#https://github.com/agorenst/maxflow/blob/master/maxflow.py
# iterator over edges of graph
def edges(graph):
    for u in graph.keys():
        for v in graph[u]:
            yield (u,v)

# dumb utility
def compute_delta(G,s):
    maxweight = max(G[s].values())
    delta = 1
    while delta * 2 < maxweight: delta *= 2
    return delta

# find and generate an augmenting path in G,
# further constrained that all the edges have
# a "high enough" weight.
def scaled_s_t_path(G, delta, s, t):
    wq  = [s] # workqueue
    seen = set([s])
    prev = {}
    while wq:
        u = wq.pop()
        for v in G[u]:
            if v not in seen and G[u][v] >= delta:
                seen.add(v)
                prev[v] = u
                if v == t:
                    break
                wq.append(v)
    path = []
    if t not in prev: return path

    v = t
    while v != s:
        path.append((prev[v], v))
        v = prev[v]
    path.reverse()
    return path

# given an augmenting path, push as much flow as
# possible throguh it.
def augment(G, P):
    # the map makes a list of all edge-weights in P
    bottleneck = min(map(lambda e : G[e[0]][e[1]], P))
    for u, v in P:
        G[u][v] -= bottleneck
        G[v][u] += bottleneck
    

# Our scaling max-flow! Observe that R is a different
# map type: it maps (u,v) -> weight, no adjacency structure.
def max_flow(G, s, t):
    R = { edge : G[edge[0]][edge[1]] for edge in edges(G) }
    delta = compute_delta(G,s)
    while delta >= 1:
        augpath = scaled_s_t_path(G, delta, s, t)
        while augpath != []:
            #print augpath, min(map(lambda e : G[e[0]][e[1]], augpath))
            augment(G, augpath)
            augpath = scaled_s_t_path(G, delta, s, t)
        delta /= 2

    return { e : R[e] - G[e[0]][e[1]] for e in R.keys() if R[e] >= G[e[0]][e[1]]}

def solve():
    N,P = readlist() #N: the number of ingredients, and P, the number of packages of each ingredient
    R = readlist()
    mx = [readlist() for _ in range(N)]
    
    G = defaultdict(lambda : defaultdict(float))
    s,t = (-1,-1),(100,100)
    Rmi = [v*1.1 for v in R]
    Rma = [v*0.9 for v in R]

    def trav(y,x,mic,mac):
        if y==0:
            G[s][(x,y)]=1
        if y==N-1:
            if mic<=mac:
                G[(x,y)][t]=1
            return
        for xx in range(P):
            yy=y+1
            mic2,mac2 = math.ceil(mx[yy][xx]/Rmi[yy]),math.floor(mx[yy][xx]/Rma[yy])
            #print(xx,yy,mic,mic2,mac,mac2)
            mic2,mac2 = max(mic2,mic),min(mac2,mac)
            if mic2<=mac2:
                G[(x,y)][(xx,yy)]=1
                trav(yy,xx,mic2,mac2)
            
    for x in range(P):
        y = 0
        mic,mac = math.ceil(mx[y][x]/Rmi[y]),math.floor(mx[y][x]/Rma[y])
        trav(y,x,mic,mac)

    return sum(v for k,v in max_flow(G, s, t).items() if k[1]==t)

start = time.clock()
for t in range(read()):
    printd('Case #{}: {}'.format(t+1, solve()))
print(time.clock()-start, file=sys.stderr)
