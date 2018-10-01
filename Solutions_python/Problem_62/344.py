for t in range(int(raw_input())):
    n = int(raw_input())
    x = {}
    y = {}
    sec = 0
    for i in range(n):
        h1,h2 = (int(i) for i in raw_input().split())
        x[h1] = 1
        y[h2] = 1

        xx = len ([f for f in x.keys() if f > h1])
        yy = len ([f for f in y.keys() if f < h2])
        s1 = min(xx, yy)

        xx1 = len ( [f for f in x.keys() if f<h1] )
        yy1 = len ( [f for f in y.keys() if f>h2] )
        s2 = min(xx1, yy1)

        l = [ k for k in [s1, s2] if k > 0]
        if (len(l)>0): sec += min(l)

    print "Case #%d:" % (t+1), sec
