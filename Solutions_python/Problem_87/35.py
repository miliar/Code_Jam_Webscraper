import sys
rl = lambda: sys.stdin.readline().strip()

t = int(rl())
for cc in range(t):
    length, walk, run, maxrun, n = map(int, rl().split())
    ways = [map(int, rl().split()) for i in xrange(n)]
    span = sum(w[1] - w[0] for w in ways)
    ways.append((0, length-span, 0))
    ways.sort(cmp=lambda a,b:cmp(a[2],b[2]))
    time = 0.0
    for begin, end, speed in ways:
        span = end - begin
        will_run = min(maxrun, float(span) / (speed + run))
        ran = will_run * (speed + run)
        walk_dist = span - ran
        #print begin, end, speed
        #print "span %g will_run %g ran %g walk_dist %g" % (span, will_run,
        #        ran, walk_dist)
        time += will_run + walk_dist / float(walk + speed)
        maxrun -= will_run
    print "Case #%d:" % (cc+1),
    print "%.10lf" % time

