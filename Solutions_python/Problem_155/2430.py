#!/usr/bin/env python
#author: Chen Zhao
import sys

def solve(case, maxShy, audiences):
    stand = 0
    add = 0
    for i, c in enumerate(audiences):
        if stand>=i:
            stand += c
        else:
            add += (i-stand)
            stand = i + c
    result = add

    print 'Case #%d: %d'%(case, result)


def main():
    T = int(sys.stdin.next())
    for i in range(T):
        line = sys.stdin.next().split()
        maxShy = int(line[0])
        audiences = map(int, line[1])
        solve(i+1, maxShy, audiences)


if __name__=='__main__':
    main()

