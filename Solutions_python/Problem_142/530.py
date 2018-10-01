import os
import re
import math
from collections import deque
import heapq
import time

# def function():
#     return False


def main(fin, fout):
    start = time.clock()
    fin = open(fin, 'r')
    fout = open(fout, 'w')
    k = int(fin.readline())
    for i in range(k):
        flag = True
        n = int(fin.readline())
        aa = []
        cc = []
        for ii in range(0, n):
            b = list(fin.readline().rstrip())
            a, c = [], []
            a.append(b[0])
            c.append(1)
            idx = 0
            last = b[0]
            for j in range(1, len(b)):
                if b[j] != last:
                    idx += 1
                    a.append(b[j])
                    c.append(1)
                    last = b[j]
                else:
                    c[idx] += 1
            aa.append(a)
            cc.append(c)

        for ii in range(1, n):
            if len(aa[ii]) != len(aa[ii-1]):
                flag = False
                break
            for j in range(0, len(aa[ii])):
                if aa[ii][j] != aa[ii-1][j]:
                    flag = False
                    break

        cost = 0
        if flag is True:
            for j in range(0, len(aa[0])):
                sum = 0
                for ii in range(0, n):
                    sum += cc[ii][j]
                avg = int(sum/n)
                for ii in range(0, n):
                    cost += abs(cc[ii][j] - avg)


        fout.write('Case #' + str(i + 1) + ': ')

        if flag is False:
            fout.write('Fegla Won' + '\n')
        else:
            fout.write(str(cost) + '\n')

        if flag is False:
            print('Case #' + str(i + 1) + ': ' + 'Fegla Won')
        else:
            print('Case #' + str(i + 1) + ': ' + str(cost))

        #output

        if i % 10 == 9:
            print('Case #' + str(i + 1) + '/' + str(k) + ' ' + 'finished, %.3f' % (time.clock() - start) + ' sec taken')
    fin.close()
    fout.close()
    pass

if __name__ == '__main__':
    problem = 'A'
    _fin = problem + '/A-small-attempt0.in'
    _fout = _fin[:-2] + 'out'
    main(_fin, _fout)
