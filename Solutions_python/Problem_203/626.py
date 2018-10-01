import sys
import math


def solve(R, C, cake):
    for j in range(R):
        for i in range(C):
            initial = cake[j][i]
            if initial == '?':
                continue
            left, right, up, down = i, i, j, j
            lFlag, rFlag, uFlag, dFlag = True, True, True, True
            while lFlag and left - 1 >= 0:
                for k in range(up, down+1):
                    if cake[k][left - 1] != initial and cake[k][left - 1] != '?':
                        lFlag = False
                        break
                    elif k == down:
                        left -= 1
            while uFlag and up -1 >=0:
                for k in range(left, right+1):
                    if cake[up-1][k] != initial and cake[up-1][k] != '?':
                        uFlag = False
                        break
                    elif k == right:
                        up -= 1
            while rFlag and right + 1 < C:
                for k in range(up, down+1):
                    if cake[k][right + 1] != initial and cake[k][right + 1] != '?':
                        rFlag = False
                        break
                    elif k == down:
                        right += 1
            while dFlag and down + 1 < R:
                for k in range(left, right+1):
                    if cake[down + 1][k] != initial and cake[down + 1][k] != '?':
                        dFlag = False
                        break
                    elif k == right:
                        down += 1
            for tj in range(up,down+1):
                for ti in range(left, right+1):
                    cake[tj][ti] = initial
    for j in range(R):
        print(''.join(cake[j]))

    return 0


T = int(input())
for i in range(T):
    R, C = [int(s) for s in input().split(" ")]
    cake = [[x for x in list(input())] for y in range(R)]
    print('Case #{}:'.format(i+1))
    solve(R, C, cake)