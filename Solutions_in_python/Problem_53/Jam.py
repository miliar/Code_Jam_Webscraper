


INPUT_FILE = 'A-large.in'
OUT_FILE = 'A-large.out'
rf = file(INPUT_FILE)
wf = file(OUT_FILE, 'w')

caseNum = 0
def inputs():
    global caseNum
    if caseNum == 0:
        caseNum = rf.readline().strip()
        caseNum = int(caseNum)
    for i in xrange(caseNum):
        N, K = rf.readline().strip().split()
        N = int(N)
        K = int(K)
        yield N, K

cachepow = {}
cachelight = {}

def light(N, K):
    if K == 0:
        return 'OFF'
        
    if cachelight.has_key((N, K)):
        return cachelight[(N, K)]
    else:
        powvalue = 0
        if cachepow.has_key((2, N)):
            powvalue = cachepow[(2, N)]
        else:
            powvalue = pow(2, N)
            cachepow[(2, N)] = powvalue
        if ((K+1) % powvalue) == 0:
            cachelight[(N, K)] = 'ON'
            return 'ON'
        else:
            cachelight[(N, K)] = 'OFF'
            return 'OFF'

caseIndex = 1
for N, K in inputs():
    wf.write('Case #%d: %s\n' %(caseIndex,light(N, K))) 
    caseIndex += 1

wf.close()
rf.close()
