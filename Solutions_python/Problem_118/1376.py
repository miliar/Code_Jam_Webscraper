import sys
import math

numbers = [ 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004 ]
numcases = int(sys.stdin.readline())
for c in range(numcases):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    for i in range(len(numbers)):
        if numbers[i] >= a: break
    for j in range(i, len(numbers)):
        if numbers[j] > b: break
    # print("i=%d j=%d" % (i,j))
    print("Case #%d: %d" % (c+1, j-i))
