import sys

def mustwin(n, p, a):
    if n == 1:
        return a < p
    
    half = 1 << (n - 1)
    if p <= half:
        ans = (a == 0)
    else:
        if a == 0:
            ans = True
        else:
            ans = mustwin(n - 1, p - half, (a - 1) // 2)
        
    sys.stderr.write('mustwin(' + str(n) + ', ' + str(p) + ', ' + str(a) + ') = ' + str(ans) + '\n')
    return ans
    
def maxmustwin(n, p):
    mina = 0
    maxa = (1 << n) - 1
    while mina < maxa:
        a = (mina + maxa) // 2 + 1
        if mustwin(n, p, a):
            mina = a
        else:
            maxa = a -1
    ans = mina
    sys.stderr.write('minmustwin(' + str(n) + ', ' + str(p) + ') = ' + str(ans) + '\n')
    return ans

def canwin(n, p, a):
    if n == 1:
        return a < p
    
    half = 1 << (n - 1)
    if p <= half:
        if a == (1 << n) - 1:
            ans = False
        else:
            ans = canwin(n - 1, p, (a + 1) // 2)
    else:
        if a != (1 << n) - 1:
            ans = True
        else:
            ans = (p >= (1 << n))
    
    sys.stderr.write('canwin(' + str(n) + ', ' + str(p) + ', ' + str(a) + ') = ' + str(ans) + '\n')
    return ans
        
def maxcanwin(n, p):
    mina = 0
    maxa = (1 << n) - 1
    while mina < maxa:
        a = (mina + maxa) // 2 + 1
        if canwin(n, p, a):
            mina = a
        else:
            maxa = a -1
    ans = mina
    sys.stderr.write('mincanwin(' + str(n) + ', ' + str(p) + ') = ' + str(ans) + '\n')
    return ans

casen = int(sys.stdin.readline())
for casei in range(casen):
    line = sys.stdin.readline().split()
    n = int(line[0])
    p = int(line[1])
    sys.stdout.write('Case #' + str(casei + 1) + ': ' + str(maxmustwin(n, p)) + ' ' + str(maxcanwin(n, p)) + '\n')