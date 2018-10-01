import sys

def solve(maxidx,thestr):
    need = 0
    parados = 0
    curridx = 0
    for c in thestr:
        val = int(c)
        if curridx > parados:
           nuevos = curridx - parados
           need += nuevos
           parados += val + nuevos
        else:
           parados += val
        curridx += 1

    return need


# main()

# read 1 number, use it to control the loop
for tc in xrange(1, int(sys.stdin.readline())+1):
    linea = sys.stdin.readline().split()
    A, B = int(linea[0]), linea[1]
    # print "A = ", A, " B = ", B

    best = solve(A,B)
    print 'Case #%d: %d' % (tc, best)


