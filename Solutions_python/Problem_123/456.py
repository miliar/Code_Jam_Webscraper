import sys

import math
log2 = lambda x: math.log(x,2)

def mult_times(A, B):
    B = B+1
    i = int(math.ceil(log2(B-1) - log2(A-1)))
    newA = 2**i * (A-1) + 1
    #print "my %s next %s, jump %s to %s" % (A,B,i,newA)
    return i, newA

def mote(A, i, arr):
    if A == 1:
        return len(arr)
    if i == len(arr):
        return 0
    #print 'at %s with A %s opponenet %s' % (i, A , arr[i])
    if A > arr[i]:
        return mote(A + arr[i], i+1, arr)
    add_between, newA = mult_times(A, arr[i])
    return min(
        1 + mote(A, i+1, arr),
        add_between + mote(newA + arr[i], i+1, arr)
    )

f = open(sys.argv[1])

T = int(f.readline().strip())
for i in xrange(T):
    A, N = (int(n) for n in f.readline().strip().split(' '))
    arr = [int(n) for n in f.readline().strip().split(' ')]
    assert(len(arr) == N)
    arr = sorted(arr)
    #print 'arr is %s' % arr
    print 'Case #%s: %s' % (i+1, mote(A, 0, arr))
