def go(N, K):
    ans = K&(2**N-1) == 2**N-1
    return ans and 'ON' or 'OFF'

import sys

def main():
    T = int(sys.stdin.readline())
    for c in xrange(T):
        N, K = map(int, sys.stdin.readline().split())
        print "Case #%d: %s" % (c+1, go(N, K))

if __name__ == "__main__":
    main()
