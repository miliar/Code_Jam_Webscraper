import sys
fid = open(sys.argv[1])
T = int(fid.next().strip())
for i, l in enumerate(fid):
    n, k = map(int, l.strip().split())
    testv = (1<<n)-1
    if (k & testv) == testv: print 'Case #'+str(i+1)+': ON'
    else : print 'Case #'+str(i+1)+': OFF'
