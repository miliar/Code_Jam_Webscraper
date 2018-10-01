import sys
fin = open(sys.argv[1], 'r')

T = int(fin.readline())
for i in xrange(T):
    R, k, N = [int(x) for x in fin.readline().split()]
    g = [int(x) for x in fin.readline().split()]
    
    c = [None]*N
    cur = 0
    total = 0
    total_rides = 0
    while total_rides < R and c[cur] is None:
        money = 0
        steps = 0
        j = cur
        while steps < N:
            if money + g[j] > k:
                break
            money += g[j]
            j += 1
            if j == N:
                j = 0
            steps += 1

        c[cur] = (money, total, j, total_rides)
        total += money
        total_rides += 1
        cur = j
        
    #print c

    if total_rides < R:
        cycle_length = total_rides - c[cur][3]
        cycle_money = total - c[cur][1]
        
        available_cycles = (R - total_rides) // cycle_length
        total += available_cycles * cycle_money
        total_rides += available_cycles * cycle_length

    while total_rides < R:
        total += c[cur][0]
        total_rides += 1
        cur = c[cur][2]
        
    print 'Case #%d: %d' % (i+1, total)