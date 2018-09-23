from __future__ import print_function
s = """3
3 1
2 3
2 4
4 4
-1 1 -1
-1 -1 1
-1 -1 -1
1 3
4 1
13 10
1 1000
10 8
5 5
-1 1 -1 -1
-1 -1 1 -1
-1 -1 -1 10
-1 -1 -1 -1
1 4
4 3
30 60
10 1000
12 5
20 1
-1 10 -1 31
10 -1 10 -1
-1 -1 -1 10
15 6 -1 -1
2 4
3 1
3 2"""
s = open('C-small-attempt0.in').read()
# s = open('C-large.in').read()
"""
Case #1: 0.583333333
Case #2: 1.2
Case #3: 0.51 8.01 8.0
"""
import sys
import math

ss = s.split('\n')
T = int(ss[0])

f = open('C.out', 'w')
# f = sys.stdout

def bfs(N, Q, D, E, S, U, V):
    D_ = []
    rew_D = []
    # copy d
    for n in range(N):
        D_.append([])
        rew_D.append([])
        for n2 in range(N):
            D_[n].append(-1)
            rew_D[n].append(-1)
    all_visited = {}
    for n in range(N):
        # calc bfs for each horse
        visited = {n:0}
        nodes = set(range(N))
        dist = [-1 for i in range(N)]
        path = [-1 for i in range(N)]
        dist[n] = 0
        path[n] = -1
        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node
            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in range(N):
                if D[min_node][edge] != -1:
                    w = current_weight + D[min_node][edge]
                    if w > E[n]:
                        break
                    elif edge not in visited or w < visited[edge]:
                        visited[edge] = w
                        path[edge] = min_node
                        if D_[min_node][edge] < S[n]:
                            D_[min_node][edge] = float(S[n])
        for k in visited:
            visited[k] /= float(S[n])
            rew_D[n][k] = visited[k]
        # print(visited)
        # print(path)
        all_visited[n] = visited
    # for d in D:
    #     print(d)
    # for d in D_:
    #     print(d)
    # for d in rew_D:
    #     print(d)
    for u, v in zip(U, V):
        visited = {u-1: 0}
        nodes = set(range(N))
        dist = [-1 for i in range(N)]
        path = [-1 for i in range(N)]
        dist[u-1] = 0
        path[u-1] = -1
        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node
            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in range(N):
                if rew_D[min_node][edge] != -1:
                    w = current_weight + rew_D[min_node][edge]
                    if edge not in visited or w < visited[edge]:
                        visited[edge] = w
                        path[edge] = min_node
        print(visited[v-1], end=' ', file=f)
idx = 1
for j in range(0, T):
    [N, Q] = [int(s) for s in ss[idx].split(' ')]
    idx += 1
    E = []
    S = []
    for n in range(N):
        Ei, Si = [int(s) for s in ss[idx].split(' ')]
        E.append(Ei)
        S.append(Si)
        idx += 1
    D = []
    for n in range(N):
        D.append([])
        Dn = [int(s) for s in ss[idx].split(' ')]
        idx += 1
        for n2 in range(N):
            D[n].append(Dn[n2])
    U = []
    V = []
    for q in range(Q):
        [Uk, Vk] = [int(s) for s in ss[idx].split(' ')]
        U.append(Uk)
        V.append(Vk)
        idx += 1
    print('Case #%d:' % (j + 1), end=' ',file=f)
    bfs(N, Q, D, E, S, U, V)
    print(file=f)
