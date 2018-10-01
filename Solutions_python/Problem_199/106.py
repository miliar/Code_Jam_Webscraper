for tc in range(1, int(raw_input())+1):
    s, k = raw_input().split()
    s = map(ord, s)
    k = int(k)
    last = len(s)-k+1
    i = 0
    flips = 0
    while i < last:
        if s[i] == 45: # '-'
            flips += 1
            j = 0
            while j < k:
                s[i+j] ^= 6
                j += 1
        i += 1
    if 45 in s[last:]:
        print "Case #%d: IMPOSSIBLE" % tc
    else:
        print "Case #%d: %d" % (tc, flips)

