from __future__ import division
T = input()
for k in xrange(T):
    X, S, R, t, N = map(int, raw_input().split())
    W = [map(int, raw_input().split()) for i in xrange(N)]
    W.append([0, X - sum(w[1] - w[0] for w in W), 0])
    def compare (a, b):
        case1 = 1/(a[2] + S) + 1/(b[2] + R)
        case2 = 1/(a[2] + R) + 1/(b[2] + S)
        return cmp(case1, case2)
    W.sort(cmp=compare)
    y = 0
    while len(W) > 0:
        w = W.pop()
        dist = w[1] - w[0]
        run_dist = (R + w[2]) * t
        if run_dist > dist:
            run_time = dist / (R + w[2])
            t -= run_time
            y += run_time
        else:
            dist -= run_dist
            y += t
            t = 0
            y += dist / (S + w[2])
    print "Case #%s: %s" % (k+1, y)