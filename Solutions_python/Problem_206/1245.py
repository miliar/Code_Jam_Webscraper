t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    D, N = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    time = []
    for n in xrange(N):
        K, S = [int(s) for s in raw_input().split(" ")]
        time.append(float(D-K)/S)

    print "Case #{}: {}".format(i, D / max(time))