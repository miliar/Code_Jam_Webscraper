
import sys
import math

fin = sys.stdin
fout = sys.stdout


def reduction_cost(start, to):
    if start<=to: return 0
    return int(math.ceil(float(start)/to))-1
    


T = int(fin.readline())
for t in range(T):
    D = fin.readline()
    P = map(int, fin.readline().strip().split())
    
    mintime = max(P)
    for level in range(1, max(P)+1):
        time = level + sum(reduction_cost(p, level) for p in P)
        mintime = min(mintime, time)
    
    fout.write("Case #%i: %i\n" % (t+1, mintime))
    
