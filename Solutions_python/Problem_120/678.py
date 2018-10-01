import sys
import math

def num_black_circles(r, t):

    ring = 0

    while True:
        area = (r + 2*ring + 1)**2 - (r + 2*ring)**2
        #print 'ring', ring, 'area needed', area, 'ink', t
        if t >= area:
            t -= area
            ring += 1
        else:
            break

    return ring


if __name__ == '__main__':

    N = int(sys.stdin.readline().strip())

    for i in range(N):
        r, t = map(int, sys.stdin.readline().split())
        print 'Case #%s: %s' % (i+1, num_black_circles(r, t))

