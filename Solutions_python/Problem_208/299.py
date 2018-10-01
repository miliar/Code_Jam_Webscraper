T = int(raw_input())
from heapq import heappop, heappush

for i in xrange(T):
    N, Q = map(int, raw_input().split(' '))
    horses = [(-1,-1)]
    for j in xrange(N):
        E, S = map(int, raw_input().split(' '))
        horses.append((E, S))
    dist = []
    adj = ['n00b']
    for j in xrange(N):
        neigh = map(int, raw_input().split(' '))
        dist.append(neigh)
        ne = []
        for x, n in enumerate(neigh):
            if n >= 0:
                ne.append((x+1, n))
        adj.append(ne)
    #print adj
    outputs = []
    for j in xrange(Q):
        U, V = map(int, raw_input().split(' '))
        def compute(U, V):
            q = []
            horse = horses[U]
            curr = U
            neigh = adj[curr]
            visited = set()
            visited.add(U)
            for n in neigh:
                if n[0] not in visited and horse[0] >= n[1]:
                    heappush(q, (float(n[1])/horse[1], horse[0]-n[1], horse[1], n[0]))
            state = [0, 1, 1, U]
            while (curr!=V and q):
                state = heappop(q)
                curr = state[3]
                visited.add(curr)
                neigh = adj[curr]
                horse = horses[curr]
                for n in neigh:
                    if n[0] not in visited:
                        if horse[0] >= n[1]:
                            heappush(q, (state[0] + float(n[1])/horse[1], horse[0]-n[1], horse[1], n[0]))
                        if state[1] >= n[1]:
                            heappush(q, (state[0] + float(n[1]) / state[2], state[1] - n[1], state[2], n[0]))
            if curr!=V:
                return float('inf')
            return state[0]
        outputs.append(str(round(compute(U, V), 6)))
        #print arr
    print 'Case #' + str(i + 1) + ': ' + ' '.join(outputs)