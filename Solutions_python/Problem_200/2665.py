import itertools

ntests = int(raw_input())

for l in xrange(1,ntests+1):
    n = int(raw_input())
    
    lastTidy = 1
    for counter in xrange(1, n+1):
        numstr = str(counter)

        increasing = True
        for (a,b) in itertools.izip(numstr, numstr[1:]):
            if a > b:
                increasing = False
                break
                
        if increasing:
            lastTidy = counter

    print "Case #{}: {}".format(l, lastTidy)
