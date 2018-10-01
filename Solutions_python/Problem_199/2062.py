def isFlip(i, flips, K):
    if i < 0 or i > len(flips)-K:
        return 0
    else:
        return flips[i]

T = int(input())
for case in range(T):
    inp = input().strip().split()
    S = inp[0]
    K = int(inp[1])
    states = [c == '+' for c in S]
    flips = [0 for c in S]
    flipstate = 0
    nflips = 0
    for i in range(len(states)):
        state = states[i]
        flipstate = flipstate ^ isFlip(i-K, flips, K)
        if not (state ^ flipstate):
            if i > len(flips)-K:
                nflips = "IMPOSSIBLE"
            else:
                nflips += 1
                flips[i] = 1
                flipstate = not flipstate
    print("Case #"+str(case+1)+": "+str(nflips))

            
