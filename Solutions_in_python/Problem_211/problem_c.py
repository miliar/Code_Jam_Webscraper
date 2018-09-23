from collections import deque  # @UnresolvedImport
from sys import stdin
import operator

DEBUG = False

def main():
    t = int(stdin.readline().strip())
    for kk in xrange(1, t+1):
        n, k = (int(s) for s in stdin.readline().strip().split(' '))
        u = float(stdin.readline().strip())
        p = deque(sorted(float(s) for s in stdin.readline().strip().split(' ')))
        if n == k:
            num_cores = 0
            last_p = 0.0
            while p and u > 0.0:
                # All probabilities increased to at least last_p
                next_p = p.popleft()
                if next_p == last_p:
                    if DEBUG:
                        print "Same probability {}".format(next_p)
                    num_cores += 1
                    continue 
                if num_cores and u/num_cores < next_p - last_p:
                    if DEBUG:
                        print "Upping probability slightly to {}".format(last_p + u/num_cores)
                    last_p += u/num_cores
                    u = 0.0
                    p.appendleft(next_p)
                    break
                else:
                    if DEBUG:
                        print "Upping probability to {}".format(next_p)
                    u -= (next_p - last_p) * num_cores
                    last_p = next_p
                    num_cores += 1
            if u > 0.0:
                last_p = min(last_p + u / num_cores, 1.0)
            assert u <= 0.0 or not p, "{} {}".format(u, p)
            v = (last_p ** num_cores) * reduce(operator.__mul__, p, 1)
            assert v <= 1.0
            print "Case #{}: {}".format(kk, v)
        else:
            print "Case #{}: Not implemented".format(kk)

main()
