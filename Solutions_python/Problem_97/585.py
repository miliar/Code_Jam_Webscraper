import sys

N = int(sys.stdin.readline()[:-1])

def isrnumber(r, B):
    p = str(r)
    pp = p + p
    ret = set()
    for i in range(1, len(p)):
        s = pp[i:i+len(p)]
        if s[0]=='0':
            continue
        n = int(s)
        if n <= B and n > r:
            ret.add(n)
    return len(ret)

for i in range(N):
    line = sys.stdin.readline()[:-1]
    fs = line.split()
    A = int(fs[0])
    B = int(fs[1])
    ret = 0
    for ii in range(A, B):
        ret += isrnumber(ii, B)
    print "Case #%d: %s" % (i+1, ret)

