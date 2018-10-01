#!/usr/bin/python2.7
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for tc in range(n):
        parts = sys.stdin.readline().split()
        res, cnt = 0, 0
        for i, c in enumerate(parts[1]):
            if cnt < i and int(c) > 0:
                res += i - cnt
                cnt += i - cnt
            cnt += int(c)
        print "Case #%d: %d" % (tc + 1, res)
