C = input()

for c in range(C):
    N, K, B, T = map(int, raw_input().split(" "))
    X = map(int, raw_input().split(" "))
    V = map(int, raw_input().split(" "))
    times = [0.0] * N
    for i in range(N):
        times[i] = float(B - X[i]) / float(V[i])

    #print times

    swap_count = 0
    impossible = False
    for i in range(N-1,N-1-K,-1):
        if times[i] > T:
            for j in range(i-1,-1,-1):
                if times[j] <= T:
                    break
            else:
                impossible = True
                break
            for k in range(j,i):
                times[k], times[k+1] = times[k+1], times[k]
                swap_count += 1
                #print times

    if impossible:
        print "Case #%d: IMPOSSIBLE" % (c+1)
    else:
        print "Case #%d: %d" % (c+1, swap_count)
            
            
            
