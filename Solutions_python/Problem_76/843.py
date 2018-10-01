
from copy import copy
import numpy as np
import itertools as iter



def seanCount(vals):

    return reduce(np.bitwise_xor, vals)


def mysetdiff(a, b):
    c = copy(a)
    for i in b:
        if i in c:
            c.remove(i)
    return c

fin = file("C-small-0.in")
#fin = file("C-small-0.example")
fout = file ("C-small-0.out", "w")

ncase = int(fin.readline().strip())

for i in range(ncase):
    fin.readline()
    vals = map(int, fin.readline().strip().split())

    if seanCount(vals):
        outStr = "Case #%i: NO" % (i+1)
    else:
        realVals = []
        for j in range(1, len(vals)/2+1):
            for a in iter.combinations(vals, j):
                #b = np.setdiff1d(vals, a)
                b = mysetdiff(vals, a)
                #print i, a, b

                if seanCount(a) == seanCount(b):
                    realVals.append(max( sum(a), sum(b) ))

        if len(realVals):
            outStr = "Case #%i: %i" % (i+1, max(realVals))
        else:
            outStr = "Case #%i: NO" % (i+1)

    print outStr
    fout.write(outStr + "\n")

fin.close()
fout.close()

