#!/bin/python3
import math


T = int(input().strip())
for test in range(T):
    N, K = [int(x) for x in input().split()]
    cakes = []
    for i in range(N):
        R, H = [int(x) for x in input().split()]
        cakes.append((math.pi * R**2, 2 * math.pi * R * H))
    cakes = sorted(cakes, key=lambda x: x[1])
    cakes = sorted(cakes, key=lambda x: x[0])
    # print(cakes)
    heights = {}
    # heights[K - 1] = sum([cakes[x][1] for x in range(K)])
    for i in range(K, N):
        hs = [cakes[x][1] for x in range(i)]
        hs.sort()
        # print(hs)
        # print(hs[:-(K-1)])
        if K>1:
            heights[i] = sum(hs[-(K-1):]) + cakes[i][1]
        else:
            heights[i] = cakes[i][1]
    # print(heights)
    scores = []
    initscore = cakes[K - 1][0] + sum([cakes[x][1] for x in range(K)])
    scores.append(initscore)
    for i in range(K, N):
        scores.append(cakes[i][0] + heights[i])
    # print(scores)
    ans = max(scores)
    # initscore = cakes[K - 1][0] + sum([cakes[x][1] for x in range(K)])
    # scores = {}
    # scores[K - 1] = initscore
    # sets = {}
    # sets[K - 1] = [x for x in range(K)]
    # # print(cakes)
    # for st in range(K, N):
    #     score = scores[st - 1]
    #     nscore = score
    #     out = st
    #     key = -1
    #     # print(sets, score)
    #     for x in range(K):
    #         val = (sum(cakes[st]) - cakes[st - 1][0] -
    #                cakes[sets[st - 1][x]][1])
    #         if score + val > nscore:
    #             nscore = score + val
    #             out = sets[st - 1][x]
    #     scores[st] = nscore
    #     nset = sets[st - 1]
    #     if out != st:
    #         nset.append(st)
    #         nset.remove(out)
    #     sets[st] = nset
    # ans = scores[N - 1]
    print('Case #%d: %f' % ((test + 1), ans))
