
def process(q, qlist):
    res = 0
    uniq_se = {}
    for ele in qlist:
        uniq_se[ele] = 0
        if len(uniq_se) == q:
            uniq_se = {ele : 0}
            res+=1
    return res

fin = open("A-large.in")
N = int(fin.readline()[:-1])
for i in xrange(N):
    s = int(fin.readline()[:-1])
    qlist = []
    
    for tt in xrange(s):
       fin.readline()
    q = int(fin.readline()[:-1])
    for tt in xrange(q):
        qlist.append(fin.readline()[:-1])
    print "Case #%d: %d" % (i+1, process(s, qlist))

