T = int(raw_input())

for i in range(1,T+1):
    R, k, N = [ int(x) for x in raw_input().split() ]
    l = [ int(x) for x in raw_input().split() ]

    Q = l
    boarded = []
    money = 0
    for j in range(0, R):
#        print 'Q: ', Q
        for x in Q:
            if sum(boarded + [x]) <= k:
                boarded.append(x)
            else:
                break
#        print 'Boarded: ', boarded
        h = len(boarded)
        Q = Q[h:] + boarded
        money += sum(boarded)
        boarded = []
    print 'Case #%d: %d'%(i, money)

