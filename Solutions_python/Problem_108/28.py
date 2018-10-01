################################################################
def solve():
    inf = 100000000000
    N = int(input.readline())
    d,l = range(N), range(N)
    for i in range(N):
        d[i], l[i] = [int(x) for x in input.readline().split(' ')]
    D = int(input.readline())
    d.append(D)
    l.append(0)
    r = [inf for i in range(N+1)] # required swing length on this rope to make it
    r[N] = 0
    for i in range(N,-1,-1):
        for j in range(i+1,N+1):
            # What is required to reach j and is it enough?
            L = d[j] - d[i] # Length of rope required
            if L > l[i]: # No way
                break
            if L < r[j]: # not a good enough rope
                continue
            r[i] = min(r[i], L)
    return (r[0] <= l[0] and r[0] <= d[0]) and "YES" or "NO"
################################################################

from datetime import datetime
time_start = datetime.today()
def now(): return datetime.today() - time_start 

import sys
infilename = sys.argv[1]
outfilename = infilename.replace('.in','.out')

input = open(sys.argv[1], 'r')
output = open(sys.argv[1].replace('.in','.out'), 'w')
n = int(input.readline())

for i in range(1,n+1):
    result = solve()
    print "Case #%d: %s \t %s" % (i, result, now())
    output.write("Case #%d: %s\n" % (i, result))
    output.flush()
