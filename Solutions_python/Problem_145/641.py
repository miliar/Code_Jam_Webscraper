import sys

def possible(a, b, ngen):
    if (ngen > 40):
        return (False, 41)

    if (a == b):
        return (True, ngen)

    if (a > b):
        (pred, gens) = possible(a - b, b, ngen + 1)
        if (pred):
            return (True, ngen)

        return (False, -1)

    return possible(2 * a, b, ngen + 1)


f = open(sys.argv[1])
ncases = int(f.readline()) + 1

for case in xrange(1, ncases):
    print "Case #%d: " % case,
    line = f.readline()[:-1]
    (a, b) = map(int, line.split('/'))
    if (a / b > 1):
        print "impossible"
        continue
    (ispossible, mingen) = possible(2 * a, b, 1)
    if (ispossible):
        print mingen
    else:
        print "impossible"
