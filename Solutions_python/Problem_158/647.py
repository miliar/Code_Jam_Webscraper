T = int(raw_input())
for t in xrange(T):
    X, R, C = map(int, raw_input().split())
    if X == 1:
        ans = 1
    elif X == 2:
        if R*C % 2 == 0: ans = 1
        else: ans = 0
    elif X == 3:
        if R % 3 != 0 and C % 3 != 0:
            ans = 0
        elif min(R, C) == 1:
            ans = 0
        else:
            ans = 1
    else:
        if R*C % 4 != 0: ans = 0
        elif min(R, C) <= 2: ans = 0
        else: ans = 1
    if ans == 0:
        ans = "RICHARD"
    else:
        ans = "GABRIEL"
    print "Case #{}: {}".format(t+1, ans)
