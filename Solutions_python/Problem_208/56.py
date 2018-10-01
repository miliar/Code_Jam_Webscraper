# Solution to "Pony Express" for Google Code Jam 2017
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys

infinity = 10**20 #10**9 times 100 cities, plus a margin

def cases(inputFile):
    with open(inputFile, 'r') as f:
        numCases = int(f.readline())
        for _ in range(numCases):
            n, q = [int(x) for x in f.readline().split()]
            horses = [[int(x) for x in f.readline().split()]
                      for _ in range(n)]
            links = [[int(x) for x in f.readline().split()]
                      for _ in range(n)]
            deliveries = [[int(x) for x in f.readline().split()]
                          for _ in range(q)]
            yield n, q, horses, links, deliveries

def fw(dist):
    size = len(dist)
    for u in range(size):
        for v in range(size):
            if u == v:
                dist[u][v] = 0
            elif dist[u][v] == -1:
                dist[u][v] = infinity
    for mid in range(size):
        for s in range(size):
            for d in range(size):
                if dist[s][d] > dist[s][mid] + dist[mid][d]:
                    dist[s][d] = dist[s][mid] + dist[mid][d]

def solve(n, q, horses, links, deliveries):
    fw(links)
    rides = [[-1 for _ in range(n)] for __ in range(n)]
    for s in range(n):
        for d in range(n):
            if s == d: continue
            if links[s][d] < infinity:
                if horses[s][0] >= links[s][d]:
                    rides[s][d] = float(links[s][d])/horses[s][1]
    fw(rides)
    results = []
    for s, d in deliveries:
        results.append(rides[s-1][d-1])
    return results
    return [rides[s][d] for s, d in deliveries]

with open(sys.argv[2], 'w') as f:
    for num, args in enumerate(cases(sys.argv[1])):
        result = solve(*args)
        f.write("Case #%d: %s\n"%(num+1, ' '.join(str(x) for x in result)))
