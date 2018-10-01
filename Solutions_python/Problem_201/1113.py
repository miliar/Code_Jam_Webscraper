import sys
import os
from math import floor

def solve(K, N):
    stallMap = {K: 1}
    n = N
    while n > 0:
        maxSpace = max(stallMap)
        num = stallMap[maxSpace]
        newSpace = maxSpace - 1
        lSpace = floor(newSpace / 2)
        rSpace = newSpace - lSpace
        if num >= n:
            return str(rSpace) + ' ' + str(lSpace)
        del stallMap[maxSpace]
        if lSpace in stallMap:
            stallMap[lSpace] += num
        else:
            stallMap[lSpace] = num
        if rSpace in stallMap:
            stallMap[rSpace] += num
        else:
            stallMap[rSpace] = num
        if 0 in stallMap:
            del stallMap[0]
        n -= num

def main():
    with open(sys.argv[1]) as fp:
        def readline():
            return fp.readline().strip()
        num_cases = int(readline())
        with open(os.path.splitext(sys.argv[1])[0] + '.out', 'w') as fpo:
            for i in range(num_cases):
                tmp = readline().split()
                [K, N] = [int(x) for x in tmp]
                res = "Case #%d: %s\n" % (i + 1, solve(K, N))
                print(res, end='')
                fpo.write(res)
main()
