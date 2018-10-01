import sys

def input():
    T = int(sys.stdin.readline())
    for i in range(1,T+1,1):
        R,C,W = map(int, sys.stdin.readline().split())
        print "Case #{}: {}".format(i,count(R,C,W))

def count(R,C,W):
    if C-1 > W:
        if C/W == 1:
            count = W+1
        elif C%W == 0:
            count = C/W + W - 1
        else:
            count = C/W + W
    else:
        count = C
    return count

input()