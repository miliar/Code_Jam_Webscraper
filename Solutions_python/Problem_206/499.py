t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
    D, N = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    slowest = 0
    for j in xrange(N):
        k, s = [int(s) for s in raw_input().split(" ")]
        time = float(D-k)/s
        if slowest < time:
            slowest = time
    result = D/slowest

    
    print "Case #{}: {:.6f}".format(i, result)
