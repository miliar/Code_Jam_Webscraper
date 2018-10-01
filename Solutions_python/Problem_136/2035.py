import sys

T = int(sys.stdin.readline())

for t in range(1, T+1):
    f = 2.0
    C,F,X = [float(y) for y in sys.stdin.readline().split(' ')]
    s = 0.0
    while True:
        a = X / f
        b = C / f
        c = b + (X / (f + F))
        if a <= c:
            s += a
            break
        else:
            f += F
            s += b
    print 'Case #%d: %s' % (t, round(s, 7))
