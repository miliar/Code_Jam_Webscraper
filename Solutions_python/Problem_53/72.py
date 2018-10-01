print "\n".join([(lambda c, a: "Case #%d: %s" % (c+1, "ON" if (a[1]&(2**a[0]-1))==(2**a[0]-1) else "OFF"))(c, map(int, raw_input().split())) for c in xrange(int(raw_input()))])
