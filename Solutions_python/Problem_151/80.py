#!/usr/bin/python

import sys

mem = {}

def explore(N, S, assignment, k):
    key = "/".join(map(str, assignment)) + "#" + str(k)
    
    if key in mem:
        return mem[key]
    else:
        e = explore_(N, S, assignment, k)
        mem[key] = e
        return e

def explore_(N, S, assignment, k):
    if k > 0:
        (gm, gmc) = (0, 0)
        for i in range(N):
            (max, maxcount) = explore(N, S, assignment + [i], k-1)
            if max > gm:
                gm = max
                gmc = maxcount
            elif max == gm:
                gmc += maxcount
        return (gm, gmc)
    else:
        #print(assignment)
        servers = []
        for i in range(N):
            servers.append(set())
        for i in range(M):
            # add string #i and prefixes to server #assignment[i]
            str = S[i]
            for j in range(0, len(str)+1):
                #print(str, str[:j])
                servers[assignment[i]].add( str[:j] )
        count = 0
        for s in servers:
            count += len(s)

        #print(servers, count)

        return (count, 1)


f = sys.stdin

T = int(f.readline())

for index in range(1, T+1):
    [M, N] = map(int, f.readline().split())
    S = []

    for i in range(M):
        S.append(f.readline().strip())
    
    mem = {}
    (max, maxcount) = explore(N, S, [], M)
    #print(mem)
    
    print("Case #{}: {} {}".format(index, max, maxcount % 1000000007))