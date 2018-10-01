# -*- coding: utf-8 -*-

T = int(raw_input())
for case in xrange(1, T + 1):
    N = int(raw_input())
    K = list(str(N))
    L = len(K)
    for i in xrange(L - 1, 0, -1):
        if K[i] < K[i - 1]:
            K[i - 1] = str(int(K[i - 1]) - 1)
            K[i] = "9"
    for i in xrange(L - 1):
        if K[i] > K[i + 1]:
            K[i + 1] = "9"
    if K[0] == "0":
        K = ["9"]*(L - 1)
    print "Case #%s: %s" % (case, "".join(K))
