#! /usr/bin/env python
import sys

sample = "sample"

if len(sys.argv) < 2:
    print "usage: %s [sample | name]" % (sys.argv[0], )
    sys.exit(1)

if sys.argv[1].lower() == "sample":
    fin = open(sample + ".in", "r") 
    fout = open(sample + ".out", "w")
else:
    fin = open(sys.argv[1], "r")
    fout = open(sys.argv[1] + ".out", "w")

size = 4
matrix = []
winner = None
case = 1
ncases = int(fin.readline())

def out(case, winner, incom):
    if winner:
         msg = "Case #%d: %s won\n" % (case, winner)
    elif incom:
        msg = "Case #%d: Game has not completed\n" % (case, )
    else:
        msg = "Case #%d: Draw\n" % (case, )
    
    fout.write(msg)

def gen_patterns(sz):
    patterns = []

    for i in xrange(0, sz, 1):
        p = [j for j in xrange(i, sz ** 2, sz)]
        patterns.append(tuple(p))
    
    for i in xrange(0, sz ** 2, 4):
        p = [j for j in xrange(i, i + sz, 1)]
        patterns.append(tuple(p))
    
    patterns.append(tuple([j for j in xrange(0, sz ** 2, sz + 1)]))
    patterns.append(tuple([j for j in xrange(sz - 1, (sz ** 2) - 1, sz - 1)]))

    return patterns

patterns = gen_patterns(size)

while True:
    line = fin.readline()
    line = line.rstrip()

    if not line:
        incomplete = "." in matrix
        
        for p in patterns:
            rc = [matrix[i] for i in p]

            if rc.count("T") > 1:
                continue

            if rc.count("T") == 1:
                if rc.count("X") == size - 1:
                    winner = "X"
                    break
                elif rc.count("O") == size - 1:
                    winner = "O"
                    break
            else:
                if rc.count("X") == size:
                    winner = "X"
                    break
                elif rc.count("O") == size:
                    winner = "O"
                    break

        out(case, winner, incomplete)

        winner = None
        matrix = []
        case += 1

        if case > ncases:
            break

    else:
        matrix.extend([c for c in line])
