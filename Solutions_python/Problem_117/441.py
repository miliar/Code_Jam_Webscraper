from collections import namedtuple
from copy import copy, deepcopy
import sys
import operator

__author__ = 'sladiwal'

fname = "test.txt"

def summ(arr, N):
    total = 0
    for x in range(N):
        total += sum(arr[x])
    return total

def minimum(N, arr):
    minm = 101
    minposx, minposy = 0, 0
    for y in range(int(N)):
        tp = map(lambda a1: a1 if a1 else 101, arr[y])
        min_index, min_value = min(enumerate(tp), key=operator.itemgetter(1))
        minm = min_value if min_value < minm else minm
        if minm == min_value:
            minposx, minposy = y, min_index
    return minm, minposx, minposy


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    f = open(fname, "r")
    T = int(f.readline())
    for x in range(T):
        N, M = f.readline().rstrip().split(' ')
        arr = []
        minm = 101
        for y in range(int(N)):
            inp = map(lambda x: int(x), f.readline().rstrip().split(' '))
            arr.append(inp)

        maxm = max(int(N), int(M))
        yeah = False
        y = 0
        while 1:
            if not summ(arr, int(N)):
                yeah = True
                break
            min_value, minposx, minposy = minimum(N, arr)
            found = True
            arr1 = deepcopy(arr)

            for a in range(int(N)):
                if arr[a][minposy] > min_value:
                    found = False
                    break
                else:
                    arr1[a][minposy] = 0

            if not found:
                found = True
                arr1 = deepcopy(arr)
                for a in range(int(M)):
                    if arr[minposx][a] > min_value:
                        found = False
                        break
                    else:
                        arr1[minposx][a] = 0

            if not found:
                break
            else:
                arr = deepcopy(arr1)

        sys.stdout.write('Case #%d: ' % (x + 1))
        if yeah:
            print "YES"
        else:
            print "NO"


