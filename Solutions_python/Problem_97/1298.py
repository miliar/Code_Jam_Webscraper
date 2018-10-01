from sets import Set
def compute_recyclable(a, m):
    stra = str(a);
    l = []
    for i in range(len(stra)-1):
        t = int(stra[i+1:]+stra[0:i+1])
        if t <= m and len(str(t)) == len(stra) and a < t:
            l.append(t);
    return l


def solve(A, B):
    t = Set();
    for i in range(A, B):
        t.update([(i, j) for j in compute_recyclable(i, B)])
    return len(t)

T = int(raw_input())
for i in xrange(T):
    a, b = [int(j) for j in raw_input().split(' ')]
    print "Case #%d: %d" % (i+1, solve(a, b))
