#!/usr/bin/env python

import sys

def main():
    num = int(sys.stdin.readline().strip())
    for i in range(num):
        line = sys.stdin.readline().strip()
        (N, K) = line.split()
        flag = True
        N = int(N)
        K = int(K)

        for j in range(N):
            if K & (1 << j) == 0:
                flag = False

        if flag:
            print "Case #%d: ON" % (i +1)
        else:
            print "Case #%d: OFF" % (i +1)

if __name__ == '__main__':
    main()
