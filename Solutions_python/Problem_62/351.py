


def in_net():

    f = open("A-small-attempt1.in", "r")

    T = int(f.readline())

    for testNum in xrange(1, T+1):

        N = int(f.readline())

        flat = set()
        ups = set()
        downs = set()

        for i in range(N):

            a, b = map(int, f.readline().split())
            line = [a,b]
            if a == b:
                flat.add(a)
            elif a > b:
                downs.add((a,b))
            else:
                ups.add((a,b))

        #print 'flat', flat
        #print 'ups', ups
        #print 'downs', downs
        
        inters = 0

        done = set()
        for up in ups:
            # Check intersects flat one.
            a, b = up
            for i in range(a, b+1):
                if i in flat:
                    #print up, i
                    inters += 1

            # Check intersects down
            for down in downs:
                if (a >= down[1] and a < down[0]) or (b <= down[0] and b > down[1]) or (a <= down[1] and b >= down[0]):
                    #print up, down
                    inters += 1

            
            for up2 in ups:
                if up != up2 and up not in done and up2 not in done:
                    if (a > up2[0] and b < up2[1]) or (a < up2[0] and b > up2[1]):
                        #print up, up2
                        inters += 1
                        done.add(up)

        done = set()
        for down in downs:
            a, b = down
            for down2 in downs:
                if down != down2 and down not in done and down2 not in done:
                    if (a > down2[0] and b < down2[1]) or (a < down2[0] and b > down2[1]):
                        print down, down2
                        inters += 1
                        done.add(down)
                        print 'inter', inters

        print "Case #%d: %d" % (testNum, inters)

in_net()
    
                    
