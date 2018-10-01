import sys
from bisect import bisect

def solveD(N, naomi, ken):
    score = 0
    for iii in range(N):
        pos = bisect(naomi, ken[-1]) # naomi's winner block
        if pos != len(naomi):
            naomi.pop(pos)
            ken.pop()
            score += 1
        else: # naomi loses, while ken lose largest block
            naomi.pop(0)
            ken.pop()
    return score

def solveW(N, naomi, ken):
    score = 0
    for w in naomi:
        pos = bisect(ken, w)
        if pos == len(ken): # pop minimum
            ken.pop(0)
            score += 1
        else:
            ken.pop(pos)
    return score

def main():
    T = int(sys.stdin.readline())
    for prob in range(T):
        N = int(sys.stdin.readline())
        naomi = [float(i) for i in sys.stdin.readline().split()]
        ken = [float(i) for i in sys.stdin.readline().split()]
        naomi.sort()
        ken.sort()
        d = solveD(N, naomi[:], ken[:])
        w = solveW(N, naomi, ken)
        print "Case #{0}: {1} {2}".format(prob + 1, d, w)

main()
