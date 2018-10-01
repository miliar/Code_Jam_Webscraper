T = int(raw_input())
for t in range(1,T+1):
    N = int(raw_input())
    swing_back = [-1]*N
    vines = [[int(x) for x in raw_input().split()] for y in range(N)]
    D = int(raw_input())
    swing_back[0] = vines[0][0]
    current = 0
    reachable = False
    farthest = 0
    done = False
    while not done:
        if swing_back[farthest]+vines[farthest][0]>=D:
            done = True
            reachable = True
        elif farthest==N-1:
            if swing_back[farthest]+vines[farthest][0]>=D:
                done = True
                reachable = True
            else:
                done = True
        else:
            if vines[farthest+1][0]<=vines[current][0]+swing_back[current]:
                farthest+=1
                swing_back[farthest] = min(vines[farthest][1], vines[farthest][0]-vines[current][0])
            else:
                if farthest==current:
                    done = True
                else:
                    current+=1
    print "Case #"+str(t)+":",
    if reachable:
        print "YES"
    else:
        print "NO"
