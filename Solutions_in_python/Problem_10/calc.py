# coding: utf-8

import os, sys, re, string


def main():
    count = int(sys.stdin.readline())
    for index in range(1, count + 1):
        P, K, L = map(int, sys.stdin.readline().strip().split(" "))
        values = map(int, sys.stdin.readline().strip().split(" "))
        if P*K < L or P*K < len(values):
            print "Case #%d: Impossible" % index
        else:
            values.sort()
            values.reverse()
            total = 0
            c = 1
            j = 0
            for v in values:
                total += c*v
                j += 1
                if j >= K:
                    j = 0
                    c += 1
            print "Case #%d: %d" % (index, total)

        
if __name__ == '__main__':
    main()

