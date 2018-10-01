#!/usr/bin/python3

t = int(input())

for i in range(0, t):
    c, f, x = [float(_) for _ in input().split(' ')]
    cf = 2.0
    ans = x / cf
    time_cost = 0.00000000
    prev = None
    while True:
        time_cost += c / cf
        cf += f
        if prev is None or prev > time_cost + x / cf:
            prev = time_cost + x / cf
        else:
            break
        ans = min(time_cost + x / cf, ans)
        #print (time_cost + x / cf)
        #time.sleep(0.5)
    print ("Case #%s: %s" % (i+1, ans))
