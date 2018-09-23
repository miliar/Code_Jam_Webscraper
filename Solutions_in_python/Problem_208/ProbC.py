ret = []

def floydwarshall(graph, n):
    dist = [[float('inf')]*(n+1) for __ in range(n+1)]
    for a in graph:
        for b in graph[a]:
            dist[a][b] = graph[a][b]
        dist[a][a] = 0
    for a in graph:
        for b in graph:
            for c in graph:
                newdist = dist[b][a] + dist[a][c]
                if newdist < dist[b][c]:
                    dist[b][c] = newdist
    return dist

with open('C-large.in', 'r') as file:
    t = int(file.readline())
    for __ in range(t):
        n, q = map(int, file.readline().split())
        graph = {i:None for i in range(n)}

        horseGas = []
        horseV = []
        for _h in range(n):
            e, s  = map(int, file.readline().split())
            horseGas.append(e)
            horseV.append(s)
        for node in range(n):
            graph[node] = {i:x for i, x in enumerate(map(int, file.readline().split())) if x != -1}

        fwDists = floydwarshall(graph, n)
        horseTime = {}

        for horse in range(n):
            horseTime[horse] = {}
            for dest in range(n):
                if fwDists[horse][dest] <= horseGas[horse]:
                    horseTime[horse][dest] = fwDists[horse][dest] / horseV[horse]

        fwHorses = floydwarshall(horseTime, n)

        tret = []
        for query in range(q):
            u, v = map(int, file.readline().split())
            tret.append(fwHorses[u-1][v-1])
        tret = ' '.join(map(str, tret))

        ret.append(tret)


with open('Cout-large.txt', 'w') as outfile:
    for i in range(t):
        outfile.write("Case #%d: %s\n" %(i+1, ret[i]))