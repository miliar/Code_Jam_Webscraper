#!/usr/bin/python

def proc():
    global v, n, k

    ans = []
    idd = 0

    while k:
        k = k -1
        idd = idd + 1
        tmp = [-1, -1]
        pos = 0

        for i in range(n):
            if v[i]: continue

            np = [0, 0]
            for j in range(i-1, -1, -1):
                if v[j]: break
                np[0] = np[0] + 1

            for j in range(i+1, n):
                if v[j]: break
                np[1] = np[1] + 1

            if min(np[0], np[1]) > min(tmp[0], tmp[1]) or min(np[0], np[1]) == min(tmp[0], tmp[1]) and max(np[0], np[1]) > max(tmp[0], tmp[1]):
                tmp = np
                pos = i

        v[pos] = 1
        ans = tmp

    return ans

t = int(input())
for i in range(1,t+1):
    inp = input().split(' ')
    n, k = (int(inp[0]), int(inp[1]))
    v = [0 for i in range(n)]
    if n == k :
        y, z = (0, 0)
    else:
        result = proc()
        y, z = (result[0], result[1])

    print('Case #%s: %d %d' % (i, z, y))
