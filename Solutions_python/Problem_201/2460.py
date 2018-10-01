t = int(input())

for i in range(1, t + 1):
    L = 0
    R = 0
    N, K = [int(s) for s in input().split(" ")]

    stalls = 'x'+'.'*N+'x'

    for p in range(K):
        mins = {}
        maxs = {}
        past_min = 0
        for S in range(len(stalls)):
            if stalls[S] == '.':
                L = 0
                R = 0
                for l in range(S-1, -1, -1):
                    if stalls[l] == 'x':
                        break
                    L += 1
                for l in range(S+1, len(stalls), 1):
                    if stalls[l] == 'x':
                        break
                    R += 1
                mins.setdefault(min(L, R), []).append(S)
                maxs.setdefault(max(L, R), []).append(S)

        minS = mins[max(mins.keys())]

        if len(minS) == 1:
            stall = minS[0]
        else:
            chance = {}
            for x in minS:
                for y in maxs:
                    if x in maxs[y]:
                        chance.setdefault(y, []).append(x)
            maxS = chance[max(chance.keys())]
            maxS.sort()
            stall = maxS[0]

        stalls = list(stalls)
        stalls[stall] = 'x'
        stalls = ''.join(stalls)

    ansL = 0
    ansR = 0
    for l in range(stall-1, -1, -1):
        if stalls[l] == 'x':
            break
        ansL += 1
    for l in range(stall+1, len(stalls), 1):
        if stalls[l] == 'x':
            break
        ansR += 1

    print("Case #{}: {} {}".format(i, max(ansL, ansR), min(ansL, ansR)))
