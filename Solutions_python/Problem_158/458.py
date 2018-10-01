
def solve(t):
    X, R, C = map(int, raw_input().strip().split())
    if R > C:
        R, C = C, R
    if X == 1:
        ans = 'GABRIEL'
    elif X == 2:
        if R == 1 and C == 1:
            ans = 'RICHARD'
        elif R == 1 and C == 3:
            ans = 'RICHARD'
        elif R == 3 and C == 3:
            ans = 'RICHARD'
        else:
            ans = 'GABRIEL'
    elif X == 3:
        if R == 2 and C == 3:
            ans = 'GABRIEL'
        elif R == 3 and C == 3:
            ans = 'GABRIEL'
        elif R == 3 and C == 4:
            ans = 'GABRIEL'
        else:
            ans = 'RICHARD'
    elif X == 4:
        if R == 3 and C == 4:
            ans = 'GABRIEL'
        elif R == 4 and C == 4:
            ans = 'GABRIEL'
        else:
            ans = 'RICHARD'
    print "Case #%d: %s" % (t, ans)


if __name__ == '__main__':
    T = int(raw_input().strip())
    for t in xrange(1, T+1):
        solve(t)
