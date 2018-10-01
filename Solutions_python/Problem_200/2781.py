t = int(raw_input())

def flip(n, i):
    for i in xrange(len(n)-1, i-1, -1):
        n[i] = '9'

for c in xrange(t):
    n = list(raw_input())
    ln = len(n)
    for i in xrange(ln-1, 0, -1):
        #print i
        if int(n[i-1]) > int(n[i]):
            #print "flip"
            flip(n, i)
            n[i-1] = str(int(n[i-1]) - 1)

    n = int("".join(n))
    print "Case #%d: %d" % (c+1, n)