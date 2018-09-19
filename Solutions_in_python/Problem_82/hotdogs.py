import sys

with open(sys.argv[1]) as f:
    T = int(f.readline().strip())
    for t in range(T):
        Cs, Ds = f.readline().strip().split()
        C = int(Cs)
        D = int(Ds)
        hotdogs = []
        for c in range(C):
            Ps, Vs = f.readline().strip().split()
            hotdogs.extend([int(Ps)] * int(Vs))
        hotdogs = [h-n*D for n, h in enumerate(hotdogs)]
        gaps = []
        prev = hotdogs[0]
        for h in hotdogs[1:]:
            gaps.append(h-prev)
            prev = h
        worst = 0
        currentScore = 0
        for g in gaps:
            currentScore += g
            if currentScore < worst:
                worst = currentScore
            if currentScore > 0:
                currentScore = 0
        print "Case #%s: %s" % (t+1, -float(worst)/2)
