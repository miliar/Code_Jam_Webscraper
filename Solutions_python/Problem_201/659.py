def readval(typ=int):
    return typ( raw_input() )

def readvals(typ=int):
    return map( typ, raw_input().split() )

from collections import defaultdict

def testcase(cas=-1):
    N, K = readvals() 
    segs = defaultdict(int) # segs[l] = number of segments with length=l
    segs[N] = 1 
    def split(l): # split a segment of l into 2 segs
        if l%2==1: return (l/2, l/2)
        else: return (l/2, l/2-1)
    while K: 
        max_len = max(segs.keys())
        n_longest = segs[max_len]
        # print segs 
        # print max_len, n_longest
        if n_longest<K: 
            K -= n_longest 
            del segs[max_len]
            l1, l2 = split(max_len) 
            segs[l1] += n_longest
            segs[l2] += n_longest
        else: 
            K = 0 
            res = '%d %d' % (split(max_len))
    print 'Case #%d: %s' % ( cas, res )

if __name__=='__main__':
    T = readval()
    for i in xrange(T):
        testcase(i+1)
