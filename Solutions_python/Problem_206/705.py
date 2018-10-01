def get_constant_speed(d, horses):
    slowest = max(horses, key=lambda (ki, si): (d-ki)/si)
    ki, si = slowest
    t = (d-ki)/si
    return "%.6f" % round(d/t, 6)


t = int(raw_input())
for i in xrange(1, t + 1):
    d, n = [int(s) for s in raw_input().split(" ")]
    horses = []
    for j in range(n):
        ki, si = [int(s) for s in raw_input().split(" ")]
        horses.append((float(ki), float(si)))
    print "Case #{}: {}".format(i, get_constant_speed(d, horses))