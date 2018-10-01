import sys

def f(r, t):
    return int((1-2*r+(4*r*r-4*r+1+8*t)**0.5)/4)

if __name__ == '__main__':
    fin = sys.stdin
    testcases = int(fin.readline())
    for i in xrange(testcases):
        arg = fin.readline().split()
        r, t = map(int, arg)
        print "Case #%d: %d" % (i+1, f(r,t))
