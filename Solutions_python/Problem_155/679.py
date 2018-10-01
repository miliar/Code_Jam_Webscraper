#!/usr/bin/env python
import sys

case_num = 1
def printres(result):
    global case_num
    print "Case #%s: %s" % (case_num, result)
    case_num += 1

def readline(): 
    return sys.stdin.readline().rstrip('\n')
def splitline(f):
    return map(f, readline().split())


def solve():
    s_max, s_i = splitline(str)
    s_num = map(int, list(s_i))
    r = 0
    s = 0
    for i in range(int(s_max)):
        s += s_num[i]
        if (s + r < i + 1):
            r += i - s - r + 1
    printres(r)

def main():
    for i in range(int(readline())): 
        solve()

if __name__ == '__main__': 
    main()

