
import sys

def calSwitches(ifp):
    S = int(ifp.readline().strip())
    se = {}
    for i in xrange(S):
        se[ifp.readline().strip()] = i
    Q = int(ifp.readline().strip())
    query = []
    for i in xrange(Q):
        query.append(se[ifp.readline().strip()])
    query.reverse()
    
    prev = []
    for i in xrange(S):
        prev.append(0)
    for q in query:
        m = 10000000
        for i, s in enumerate(prev):
            if i!=q and s<m:
                m = s
        prev[q] = m+1
    return min(prev)

def main():
    ifp = open(sys.argv[1])
    ofp = open(sys.argv[2], 'w')
    N = int(ifp.readline().strip())
    for i in range(N):
        ofp.write("Case #%d: %d\n" % (i+1, calSwitches(ifp)))
    ifp.close()
    ofp.close()

def test():
    import cStringIO
    input = '''5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
5
Yeehaw
NSM
Dont Ask
B9
Googol
7
Googol
Dont Ask
NSM
NSM
Yeehaw
Yeehaw
Googol'''
    
    ifp = cStringIO.StringIO(input)
    ofp = cStringIO.StringIO()
    for i in range(2):
        ofp.write("Case #%d: %d\n" % (i+1, calSwitches(ifp)))
    print ofp.getvalue()

#test()
main()