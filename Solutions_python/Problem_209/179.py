from math import pi
from sys import stdin


def main():
    t = int(stdin.readline().strip())
    for kk in xrange(1, t+1):
        n, k = (int(s) for s in stdin.readline().strip().split(' '))
        rh = [[int(s) for s in stdin.readline().strip().split(' ')]
              for _ in range(n)]
        rh = sorted(rh, key=lambda e: -e[0] * e[1])
        # print rh
        best = 0
        for j in xrange(n):
            v = pi * rh[j][0] * rh[j][0] + 2 * pi * rh[j][0] * rh[j][1]
            # print v, best
            count = k - 1
            for i in xrange(n):
                if count == 0:
                    break
                if i == j:
                    continue
                if rh[i][0] > rh[j][0]:
                    continue
                v += 2 * pi * rh[i][0] * rh[i][1]
                count -= 1
            if v > best:
                best = v
        print "Case #{}: {}".format(kk, best)

main()
