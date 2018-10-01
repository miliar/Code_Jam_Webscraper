import math
from decimal import *


def check_best(arr, best, k):

    if k == 0 or len(arr) == 0:
        return best
    best2 = best + arr[0][2] if best == 0 else  best + arr[0][2] - arr[0][3]
    
    result = max(check_best(arr[1:], best, k), check_best(arr[1:], best2, k-1))
    # print result
    return result
    

t = int(raw_input())
for i in range(t):
    n, k = map(int, raw_input().split())

    data = []
    for j in range(n):
        r, h = map(float, raw_input().split())
        suf =  2 * math.pi * r * h +  math.pi * math.pow(r, 2)
        penalty = math.pi * math.pow(r, 2)
        data.append((r, h, suf, penalty))

        
        

    mlst = []
    xst = []
    for j in range(n):
        maxi = min(data, key = lambda x: x[0])
        filtered = filter(lambda x: x[0] == maxi[0], data)
        maxi2 = max(filtered, key = lambda x: x[2])
        mlst.append(maxi2)
        maxic = (maxi2[0], maxi2[1], maxi2[2]- maxi2[3])
        xst.append(maxi2)
        index = data.index(maxi2)
        data = data[:index] + data[index+1:]

        # data = filter(lambda x: x[0] > maxi2[0], data)

    mlst = sorted(mlst, key = lambda x: x[0], reverse = True)
    total = check_best(mlst, 0, k)
    # mlst.reverse()
    # total = mlst[0][2]

    # xst = sorted(xst, key = lambda x: x[2])

    # # mlst = xst[n-k:]
    # # print mlst
    # # for j in range(1, len(mlst)):
    # #     r0 = math.pow(mlst[j][0], 2) * math.pi
    # #     total += (mlst[j][2] - r0)

    # # print xst
    print "Case #{0}: {1:.8f}".format(i+1, total)
        
    
        
