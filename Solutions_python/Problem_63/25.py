
    
import sys, math
f = open(sys.argv[1], "rt")
T =  int(f.next().strip())
for t in range(T):
    L, P, C = map(float, f.next().strip().split())
    c = math.ceil(math.log(P/L, C))
    count = int(math.ceil(math.log(c, 2)))
    print 'Case #%d: %d' %(t+1, count)
        
