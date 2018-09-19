import sys

def readInput(inputFile):
    f = open(inputFile)
    n = int(f.readline())
    cases = []
    lines = f.readlines()
    for j in range(n):
        d = {}
        d['R'], d['k'], d['N'] = [int(i) for i in lines[2*j].split()]
        d['q'] = [int(i) for i in lines[2*j+1].split()]
        cases.append(d) 
    f.close()
    return cases

def profit(R, k, q):
    e = 0
    for r in range(R):
        p = 0
        c = []
        while len(q) > 0 and p + q[0] <= k:
            g = q.pop(0)
            p += g
            c.append(g)
        e += p
        q.extend(c)
    return e

def themePark(inFile):
    cases = readInput(inFile)
    i = 1
    for c in cases:
        print "Case #%i: %i" % (i, profit(c['R'], c['k'], c['q']))
        i += 1
        
if __name__ == '__main__':
    if len(sys.argv) > 1:
        themePark(sys.argv[1])
