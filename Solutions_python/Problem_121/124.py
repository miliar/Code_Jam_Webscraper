import sys

N = 0
E = 0
R = 0
vals = []

memo = {}

def dp(e, i):
    if (e, i) in memo:
        return memo[(e,i)]

    if i == N:
        return 0
    m = 0
    #if e >= (E-R):
    #    m = vals[i]*(e - (E-R)) + dp(E, i+1)
    for j in xrange(e+1):
        val = vals[i]*j + dp(min(e - j + R, E), i+1)
        if val > m:
            m = val

    memo[(e,i)] = m
    #print (e,i), m
    return m

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for a in xrange(T):
        memo = {}
        E, R, N = map(int, sys.stdin.readline().split(' '))
        vals = map(int, sys.stdin.readline().split(' '))
        ans = dp(E, 0)
        print "Case #{}: {}".format(a+1, int(ans))
