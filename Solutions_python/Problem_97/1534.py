def rots(s): return [s[i:]+s[0:i] for i in range(len(s)) if s[i] != '0']
def getline(): return raw_input("")

T = int(getline())
for _TESTNUM in xrange(1,T+1):
    A,B = map(int, getline().split())
    pairs = set()
    for n in xrange(A,B+1):
        pairs.update(map(lambda x: (n, x), filter(lambda m: m>n and A<=m<=B, map(int, rots(str(n))))))
    print "Case #%d: %s" % (_TESTNUM, len(pairs))

