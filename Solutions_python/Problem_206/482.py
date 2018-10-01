# Google Code Jam Contest
# @L01cDev
# Author: Loic Boyeldieu
# Date: 22-04-2017




T = int(raw_input())
for i in range(1, T + 1):
    D, N = [int(e) for e in raw_input().split(" ")]
    horses = []
    maxTime = 0
    for h in range(N):
        K, S = [int(e) for e in raw_input().split(" ")]
        time = float((D-K))/float(S)
        if time >= maxTime:
            maxTime = time
        #horses.append((K, S))
    totalTime = float(D)/float(maxTime)
    #result = solveHorseProblem(D, horses)
    print("Case #{}: {}".format(i, totalTime))
