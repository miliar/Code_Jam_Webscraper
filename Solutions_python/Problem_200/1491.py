T = input()
for t in range(T):
    n = input()
    d = [int(x) for x in str(n)]
    for i in range(len(d) - 1):
        if d[i] > d[i + 1]:
            d[i] -= 1
            for j in range(i + 1, len(d)):
                d[j] = 9
            while i and d[i - 1] > d[i]:
                d[i] = 9
                d[i - 1] -= 1
                i -= 1
            break
    while d[0] == 0:
        del d[0]
    print "Case #%d: %s" % (t + 1, ''.join([str(x) for x in d]))
