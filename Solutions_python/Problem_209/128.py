import numpy as np
import itertools
t = int(raw_input())
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    arr = []
    for j in xrange(n):
      r, h = [int(s) for s in raw_input().split(" ")]
      bot = np.pi*r*r
      around = 2*np.pi*r*h
      arr.append([bot, around, r, h])
    arr = sorted(arr, key = lambda x : x[1], reverse=True)
    sum = 0.0
    mina = 9999999999999999999999.0
    maxs = 0.0
    for j in xrange(k):
        q = arr[j][1]
        w = arr[j][0]
        if w > maxs:
            maxs = w
        if q < mina:
            mina = q
        sum += q
    del arr[:k]
    if len(arr) > 0:
        arr = sorted(arr, key=lambda x: x[0]+x[1], reverse=True)
        if arr[0][0]+arr[0][1] - maxs > mina:
            sum += arr[0][0]+arr[0][1]
            sum -= mina
        else:
            sum += maxs
    else:
        sum += maxs


    print "Case #{}: {}".format(i, sum)