import sys
import re
import os
import time
from itertools import *
from pprint import pprint
from operator import xor


def solve():
    length = int(next(fin))
    values = map(int, next(fin).split())
    assert len(values) == length

    if reduce(xor, values) != 0:
        print>>fout, "NO"
        return

    print>>fout, sum(sorted(values)[1:])


if len(sys.argv) != 2:
    print 'specify input file'
    exit()

startTime = time.clock()

fin = open(sys.argv[1])
fout = open(os.path.splitext(sys.argv[1])[0]+'.out', 'w')

numCases = int(next(fin))
for caseNo in range(numCases):
    print '\b'*10, 100*caseNo/numCases, '%',
    print>>fout, 'Case #%s:'%(caseNo+1),
    solve()

fin.close()
fout.close()

print '\b'*10+'it took %.1fs'%(time.clock()-startTime)