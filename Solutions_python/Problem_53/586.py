"""A
   Google CodeJam 2010
"""

from datetime import datetime

state = ['OFF' , 'ON']

def routine(N, K):
    f = pow(2, N)
    return state[(K % f) == (f - 1)]

if __name__ == '__main__':
    filename = "A-large"
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline().strip())
    print c, "cases"
    for case in xrange(c):
        N, K = [int(x) for x in f.readline().split()]
        print N, K

        print >>fo, "Case #%d: %s" % (case+1, routine(N, K))

    fo.close()
    f.close()
    print datetime.now()
