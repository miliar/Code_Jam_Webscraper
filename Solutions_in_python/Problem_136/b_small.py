T = int(raw_input())
for t in xrange(T):
    R = 2.0
    [C, F, X] = [float(x) for x in raw_input().split()]
    total = 0.0
    while True:
        future  = X / (R + F)
        current = C / R
        finish  = X / R
        if (current + future) < finish:
            total += current
            R += F
        else:
            total += finish
            break
    print 'Case #{}: {}'.format(t+1, total)
