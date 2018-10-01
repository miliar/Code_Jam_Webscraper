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
        aa = 0
        a = int(fin.readline())
        for r in range(0, a-1):
            fin.readline()
        ns = [int(w)-1 for w in fin.readline().split()]
        for j in range(0, len(ns)):
            aa |= (1 << ns[j])
        for r in range(a, 4):
            fin.readline()

        bb = 0
        b = int(fin.readline())
        for r in range(0, b-1):
            fin.readline()
        ns = [int(w)-1 for w in fin.readline().split()]
        for j in range(0, len(ns)):
            bb |= (1 << ns[j])
        for r in range(b, 4):
            fin.readline()

        cc = aa & bb

        fout.write('Case #' + str(i + 1) + ': ')
        if cc == 0:
            fout.write("Volunteer cheated!")
        else:
            ccc = int(math.floor(math.log(cc)/math.log(2)))
            if cc ^ (1 << ccc) > 0:
                fout.write("Bad magician!")
            else:
                fout.write(str(ccc + 1))
        fout.write('\n')
        if i % 10 == 9:
            print 'Case #' + str(i + 1) + '/' + str(k) + ' ' + 'finished, %.3f' % (time.clock() - start) + ' sec taken'
    fin.close()
    fout.close()
    pass

if __name__ == '__main__':
    problem = 'A'
    _fin = problem + '/A-small-attempt0.in'
    _fout = _fin[:-2] + 'out'
    main(_fin, _fout)
