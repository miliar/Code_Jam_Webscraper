#!/usr/bin/env python
import numpy as np

inFile = open('in.txt', 'r')
outFile = open('out.txt', 'w')
t = int(inFile.readline())
for i in range(1, t+1):
    N, K = map(int, inFile.readline().split(' '))
    stage = int(np.ceil(np.log2(K + 1)))
    done = 2**(stage - 1) - 1
    remain = N - done
    peopleRemain = K - done
    cells = int(float(remain)/(2**(stage - 1)))
    extra = remain % (2**(stage - 1))
    if(peopleRemain <= extra):
        cells += 1
    left = cells/2
    right = left
    if(cells % 2 == 0):
        right -= 1
    outFile.write("Case #{}: {} {}\n".format(i, left, right))
    # print left, right
