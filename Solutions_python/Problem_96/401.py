#-*-coding:utf-8-*-

import os, sys

fh = open(sys.argv[1])
for t in range(int(fh.readline())):
    data = [int(x) for x in fh.readline().strip().split(' ')]
    N = data[0]
    S = data[1]
    p = data[2]
    scores = sorted(data[3:], reverse=True)
    num = 0
    thr1 = p + 2 * max(p-1,0)
    thr2 = p + 2 * max(p-2,0)
    for s in scores:
        if s >= thr1:
            num += 1
        elif s >= thr2 and S > 0:
            num += 1
            S -= 1
        else:
            break
        pass
    print('Case #{0}: {1}'.format(t + 1, num))
    pass

            
