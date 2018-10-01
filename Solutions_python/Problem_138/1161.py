import os
import re
import math
from collections import deque
import heapq
import time


def find_next_larger(x, array, p, q):
    if p > q or p >= len(array):
        return -1
    else:
        if p == q:
            if array[p] > x:
                return p
            else:
                return -1
    if array[p] > x:
        return p
    m = (p + q) / 2
    if array[m] > x:
        return find_next_larger(x, array, p, m)
    else:
        if array[m] < x:
            return find_next_larger(x, array, m + 1, q)
        else:
            return m


def get_wins(a, b):
    a, b = sorted(a), sorted(b)
    p = 0
    cnt = 0
    for i in range(0, len(a)):
        if p < len(b):
            p = find_next_larger(a[i], b, p, len(b))
        else:
            break
        if p != -1:
            cnt += 1
            p += 1
        else:
            break
    return cnt


def main(fin, fout):
    start = time.clock()
    fin = open(fin, 'r')
    fout = open(fout, 'w')
    k = int(fin.readline())
    for i in range(k):
        n = int(fin.readline())
        a = [float(w) for w in fin.readline().split()]
        b = [float(w) for w in fin.readline().split()]
        dwar = get_wins(b, a)
        war = n - get_wins(a, b)
        fout.write('Case #' + str(i + 1) + ': ')
        fout.write(str(dwar) + ' ' + str(war))
        fout.write('\n')
        if i % 10 == 9:
            print 'Case #' + str(i + 1) + '/' + str(k) + ' ' + 'finished, %.3f' % (time.clock() - start) + ' sec taken'
    fin.close()
    fout.close()
    pass

if __name__ == '__main__':
    problem = 'D'
    _fin = problem + '/D-large.in'
    _fout = _fin[:-2] + 'out'
    main(_fin, _fout)
