t = int(raw_input())
for i in xrange(1, t+1):
    N, K = [int(x) for x in raw_input().split(' ')]
    stalls = [0] * N
    stalls.insert(0, 1)
    stalls.append(1)

    for j in xrange(1, K+1):
        # each customer
        cal = []
        for x in xrange(0, len(stalls)):        
            if stalls[x] == 1:
                cal.append((-1, -1))
            else:
                # empty, calculate
                L = 0
                y = x - 1
                while True:
                    if stalls[y] == 0:
                        L += 1
                        y -= 1
                    else:
                        break
                R = 0
                y = x + 1
                while True:
                    if stalls[y] == 0:
                        R += 1
                        y += 1
                    else:
                        break
                cal.append((L, R))
        Max = -1
        index = -1
        for x in xrange(len(cal)-1, -1, -1):
            m = min(cal[x])
            M = max(cal[x])
            if m > Max:
                Max = m
                index = x 
            elif m == Max:
                if M > max(cal[index]):
                    Max = m
                    index = x
        
        max_c = max(cal[index])
        min_c = min(cal[index])
        stalls[index] = 1
    print "Case #" + str(i) + ": " + str(max_c)+" " +str(min_c)
