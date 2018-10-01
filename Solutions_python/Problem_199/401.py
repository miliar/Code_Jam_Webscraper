import sys

t = int(sys.stdin.readline().strip())

for i in xrange(t):
    s, k = sys.stdin.readline().strip().split()
    s = list(s)
    k = int(k)

    j = 0
    cnt = 0
    while (j < len(s)):
        if (s[j] == '-'):
            if (j + k > len(s)):
                break
            for l in xrange(k):
                s[j + l] = ('+' if (s[j + l] == '-') else '-')
            cnt += 1
        j += 1

    print "Case #%d:" % (i + 1), "IMPOSSIBLE" if (j < len(s)) else cnt

