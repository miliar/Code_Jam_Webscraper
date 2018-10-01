import sys
import math

def step(N):
    p = 0
    #print N
    i = int(math.floor(math.log10(N)))
    for c in str(N):
        if c < p:
            a = (N % 10**(int(i) + 1)) + 1
            #print "subtracting", a
            N -= a
            break
        i -= 1
        p = max(p, c)
    return N

T = sys.stdin.readline()
case = 0
for line in sys.stdin:
    case += 1
    N = long(line)
    while True:
        M = step(N)
        if N == M:
            break
        N = M
    print "Case #"+str(case)+": " + str(N)
