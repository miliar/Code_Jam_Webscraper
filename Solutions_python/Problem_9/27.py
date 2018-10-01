import time

f = open("c:/users/roy/Downloads/C-small-attempt1.in")
#f = open("C:/Users/Roy/Documents/gcj/test.in.txt")

nCnt = 0
lines = f.readlines()

#print len(lines)

nCnt = int(lines[0])
#print "There are %i test cases." % nCnt
nCase = 0

#print time.ctime(time.time())

nLineNo = 1
for nCase in range(1, nCnt+1):

    K = int(lines[nLineNo])
    nLineNo = nLineNo + 1
    #print "K = %i" % K
    vals = lines[nLineNo].split()
    nLineNo = nLineNo + 1
    n = int(vals[0])
    indexes = []
    for val in vals[1:]:
        indexes.append(val)
    #print "Indexes: %s" % str(indexes)
    i = K
    soln = []
    while i > 0:
        soln.insert(0, i)
        i = i -1
        """
        # shift-left by i
        j = 0
        while j < i:
            val = soln.pop()
            soln.insert(0, val)
            j = j + 1"""
        l = len(soln)
        v = i % l
        p1 = soln[0:l-v]
        p2 = soln[l-v:l]
        #print "%s %s" % (p1, p2)
        p2.extend(p1)
        soln = p2
        #print str(soln)
    ans = []
    #print indexes
    for index in indexes:
        ans.append(str(soln[int(index)-1]))
    print "Case #%i: %s" % (nCase, " ".join(ans))
    #print time.ctime(time.time())
        