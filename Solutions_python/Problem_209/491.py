import sys
import math

def radius(t):
    return t[0]

def bestToRemove(pcs):
    minpc = pcs[0]
    mindecr = 2 * math.pi * minpc[0] * minpc[1]
    for i in range(len(pcs)):
        pc = pcs[i]
        decr = 2 * math.pi * pc[0] * pc[1]
        if i == len(pcs)-1:
            prevpc = pcs[i-1]
            decr += math.pi * (pc[0]**2 - prevpc[0]**2)
        if decr < mindecr:
            mindecr = decr
            minpc = pc
    return minpc, mindecr

def solve():
    N, K = tuple(int(st) for st in sys.stdin.readline().split())
    pancakes = []
    for i in range(N):
        pancakes += [tuple(float(st) for st in sys.stdin.readline().split())]
    pancakes.sort(key=radius)

    surf = math.pi * (radius(pancakes[-1])**2)
    for pc in pancakes:
        surf += 2 * math.pi * pc[0] * pc[1]

    for i in range(N-K):
        best, decr = bestToRemove(pancakes)
        pancakes.remove(best)
        surf -= decr

    sys.stdout.write("%.6f\n" % surf)

T = int(sys.stdin.readline())
for t in range(T):
    sys.stdout.write("Case #%d: " % (t+1))
    solve()
