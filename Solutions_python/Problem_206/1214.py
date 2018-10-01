t = int(raw_input())

for c in xrange(1, t + 1):
    dist, n = map(int, raw_input().split())
    horses = []
    for i in xrange(n):
        start, velocity = map(float, raw_input().split())
        horses.append((start, velocity))

    slowest = 0
    slowest_time = (dist - horses[0][0]) / horses[0][1]
    for i in xrange(1, n):
        time = (dist - horses[i][0]) / horses[i][1]
        if time > slowest_time:
            slowest = i
            slowest_time = time

    ret = dist / slowest_time
    print('Case #%s: %.6f' % (c, ret))

