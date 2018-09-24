# Input should be placed in file A.txt

from heapq import heappush, heappop

f = open('A.txt')
n = int(f.readline())
for case in range(n):
    print "Case #%d:" % (case+1,),
    S = int(f.readline())
    engines = {}
    for engine in range(S):
        engines[f.readline().strip()] = engine
    Q = int(f.readline())
    queries = []
    for q in range(Q):
        queries.append(engines[f.readline().strip()])
    heap = [(0, (0, i)) for i in range(S)]
    vis = [[0] * S for i in range(Q)]
    finished = False
    while not finished:
        sw, pos = heappop(heap)
        #print sw, pos
        if pos[0] == Q:
            print sw
            finished = True
        elif vis[pos[0]][pos[1]]:
            continue
        else:
            vis[pos[0]][pos[1]] = 1
            if queries[pos[0]] != pos[1] and (pos[0] + 1 == Q or not vis[pos[0]+1][pos[1]]):
                heappush(heap, (sw, (pos[0]+1, pos[1])))
            for i in range(S):
                if not vis[pos[0]][i]:
                    heappush(heap, (sw+1, (pos[0], i)))


