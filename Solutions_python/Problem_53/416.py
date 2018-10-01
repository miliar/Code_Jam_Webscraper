import sys

def getState(n, k):
    p = 2**(n)
    return ((k+1) % p) == 0

if __name__ == '__main__':
    f = open(sys.argv[1])
    
    t = int(f.readline())
    for i in xrange(t):
        n, k = map(int, f.readline().split())
        state = getState(n, k)
        if state:
            print "Case #%d: ON" % (i+1)
        else:
            print "Case #%d: OFF" % (i+1)
            
