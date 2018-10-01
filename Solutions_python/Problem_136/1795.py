def should_buy_another_farm(cookies, farms, C, F, X):
    if cookies < C:
        return False
    not_buy = (X - cookies) / (2 + farms * F)
    buy = (X - (cookies - C)) / (2 + (farms + 1) * F)
    if not_buy < buy:
        return False
    else:
        return True

sample_count = int(raw_input())
for i in xrange(1, sample_count + 1):
    C, F, X = [float(s) for s in raw_input().split(' ')]
    cookies = 0.0
    farms = 0
    seconds = 0.0
    while cookies < X:
        # print seconds, cookies
        while should_buy_another_farm(cookies, farms, C, F, X):
            # print "buy a farm at", seconds
            cookies -= C
            farms += 1
        rate = 2.0 + farms * F
        if C < X and cookies < C:
            seconds += (C - cookies) / rate
            cookies = C
        elif cookies + rate >= X:
            # print cookies, rate
            seconds += (X - cookies) / rate
            cookies = X
        else:
            seconds += 1
            cookies += rate
    print "Case #%d: %.7f" % (i, seconds)




