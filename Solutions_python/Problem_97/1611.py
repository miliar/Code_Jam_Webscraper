from sys import stdin
def readln():
    return stdin.readline().rstrip()
def readlns(num):
    return map(str.rstrip,stdin.readlines(num))

def recycles(A,B):
    assert len(A) == len(B)
    a = int(A)
    b = int(B)
    mc = 0
    for n in range(a,b):
        nn = str(n)
        prs = set()
        for i in range(1,len(A)):
            nm = nn[i:]+nn[:i]
            inn = int(nm)
            if nm in prs: continue
            prs.add(nm)
            if inn >= a and inn <= b and inn > n:
                mc += 1
    return mc


N = int(readln())
for i,ln in enumerate(readlns(N)):
    A,B = map(str.strip, ln.split())
    print "Case #%d: %d" % (i+1, recycles(A, B))
    