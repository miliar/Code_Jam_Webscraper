test = input()
for i in xrange(test):
    n = input()
    while True:
        if sorted(list(str(n))) == list(str(n)):
            break
        n -= 1
    print "Case #%d: %d" %(i+1, n)
