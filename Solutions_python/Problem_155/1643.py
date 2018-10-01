
import sys

c = 1
for testcase in [line[:-1] for line in sys.stdin.readlines()][1:]:
    X = [int(x) for x in testcase.split(" ")[1]]

    S = X[0]
    i = 1
    F = 0
    
    while i < len(X):
        if S >= i:
            S += X[i]
            i += 1
        else:
            S += 1
            F += 1

    print "Case #%s: %s" % (c, F)
    c += 1
