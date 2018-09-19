from common import nt, ni, nl, line

def are_recycled(n, m):
    n = str(n)
    m = str(m)
    if len(n) == len(m):
        for num_d in range(1, len(n)):
            recycled = n[num_d:] + n[:num_d]
            if recycled == m:
                return True
    return False
            
def num_recycled(a, b):
    count = 0
    for n in range(a, b):
        for m in range(n+1,b+1):
            if are_recycled(n, m):
                count += 1
    return count

n = ni(); nl()
for case in xrange(n):
    a = ni()
    b = ni()
    nl()
    print "Case #%s:" % (case+1),
    print num_recycled(a, b)
