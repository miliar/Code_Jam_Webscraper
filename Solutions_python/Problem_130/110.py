def findFirst1(a):
    for i in xrange(len(a)):
        if a[i] == 1:
            return i

def best(N, k):
    res = 2**N
    while k != 2**N - 1:
        res -= 2**(N-1)
        N -= 1
        k = (k+1)/2
    return res

def worst(N, k):
    res = 1
    while k > 0:
        res += 2**(N-1)
        k = (k-1)/2
        N -= 1
    return res

def printResult(z, b, w):
    print "Case #%d: %d %d" % (z + 1, b, w)

def binSearch(N, P, L, R, f):
    while R - L > 1:
        x = (R + L)/2
     #   print f(N, x)
        if f(N, x) > P:
            R = x
        else:
            L = x
    return L

#print binSearch(3, 4, 0, 7, best)

T = int(raw_input())
for z in xrange(T):
    N, P = map(int, raw_input().strip().split())
    if P == 1:
        printResult(z, 0, 0)
    elif P == 2**N:
        printResult(z, 2**N-1, 2**N-1)
    else:
        printResult(z, binSearch(N, P, 0, 2**N-1, worst), binSearch(N, P, 0, 2**N-1, best))

##print [ best(3, i) for i in xrange(8)]
##print [ worst(3, i) for i in xrange(8)]