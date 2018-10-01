import sys

f = open(sys.argv[1])
T = int(f.readline())

for t in range(T):
    r, m = map(int, f.readline().strip().split())

    R = 2 * r + 1
    cnt = 0
    while (m >= R):
        cnt += 1
        m -= R
        R += 4

    print "Case #%d: %d" % ((t + 1), cnt)

