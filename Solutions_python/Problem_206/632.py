def solve():
    D, N = [float(i) for i in raw_input().split()]
    H = []
    for i in range (int(N)):
        H.append([float(i) for i in raw_input().split()])

    s = 9999999999999999.0
    d1 = H[0][1]
    t1 = (D-H[0][0])/d1
    for h in H:
        t = (D-h[0])/h[1]
        if h[1] <= d1 and t <= t1:
            t = t1
        if D/t < s:
            s = D/t
            d1 = h[1]
            t1 = t

    return s

T=input()

for t in xrange(1,T+1):
    print("Case #%d: %f" % (t, solve()))
