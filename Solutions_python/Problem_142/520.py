import sys

f = open(sys.argv[1])
n = int(f.readline())


def compress(w):
    w_ = ""
    s = ""
    for c in w:
        if c != w_:
            w_ = c
            s += c

    return s

def runs(w):
    l = []
    cnt = 1
    w_ = w[0]
    for c in w[1:]:
        if c != w_:
            l.append(cnt)
            w_ = c
            cnt = 1
        else:
            cnt += 1

    l.append(cnt)
    return l



for t in xrange(1,n+1):
    N = int(f.readline())
    L = []
    for i in range(N):
        L.append(f.readline().strip())
    np = False
    check = compress(L[0])
    for s in L[1:]:
        if compress(s) != check:
            np = True
            break

    if np:
         print "Case #%d: Fegla Won" % (t)
    else:
        diff = 0
        for i in range(0,len(check)):
            diff += max(runs(w)[i] for w in L) - min(runs(w)[i] for w in L)
        print "Case #%d: %d" % (t,diff)

        










