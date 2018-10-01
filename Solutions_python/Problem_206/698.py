if __name__ == '__main__':
    ncases = int(raw_input())
    for case in xrange(1, ncases+1):
        d, n = map(int, raw_input().split())
        horses = []
        for i in xrange(n):
            x, v = map(int, raw_input().split())
            if x >= d: continue
            horses.append( (x, (d-x)/float(v)) )
        horses.sort()
        x, maxTime = horses.pop()
        while horses:
            x, t = horses.pop()
            if t > maxTime:
                maxTime = t
        print "Case #%d: %f" % (case, d / float(maxTime))
