import sys
f = open(sys.argv[1], 'r')
T = int(f.readline())
for t in range(T):
    (A, B, K) = [int(x) for x in f.readline().split()]

    num = 0
    for a in range(A):
        for b in range(B):
            if a & b < K:
                num += 1

    print "Case #%d: %d" % (t + 1, num)
