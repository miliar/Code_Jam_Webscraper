import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a,b)

T = int(sys.stdin.readline())
for t in range(T):
    N, L, H = map(int, sys.stdin.readline().split())
    freqs = map(int, sys.stdin.readline().split())
    p = reduce(lambda x,y : x * y, freqs)
    
    for x in range(L, H+1):
        for f in freqs:
            if x % f != 0 and f % x != 0:
                break
        else:
            print "Case #%d: %d" %(t+1, x)
            break
    else:
        print "Case #%d: NO" %(t+1)

