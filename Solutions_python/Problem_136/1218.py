__author__ = 'dshgna'

import time


def solve(C, F, X):
    n = 0
    t = C/2
    t1 = X/2
    t2 = t + (X / (2 + F))

    while(t1 > t2):
        n = n + 1
        t1 = t2
        t = t + (C / (2 + (n*F)))
        t2 = t + (X / (2 + ((n+1) * F)))

    return t1


if __name__ == "__main__":
    start = time.time()
    f = file("B-large.in")
    fout = file("B-large.out", "w+")
    T = int(f.readline())
    #print T
    for case in range(1, T+1):
        C, F, X = map(float, f.readline().split())
        #print C, F, X
        sol = solve(C, F, X)
        out = "Case #%d: %.7f \n" % (case, sol)
        fout.write(out)
    fout.close()
    f.close()
    end = time.time()
    print "Time %s:%s (%s)" % (int((end-start) / 60), int((end-start) % 60), end-start)
