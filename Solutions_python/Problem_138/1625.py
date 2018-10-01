import sys
sys.setrecursionlimit = 20000

def g1(a, b):
    res = 0
    for i in range(len(a)):
        if a[0] > b[0]:
            res += 1
            a = a[1:]
            b = b[:-1]
        else:
            a = a[1:]
            b = b[1:]
    return res

def g2(a, b):
    res = 0
    for i in range(len(a)):
        if a[-1] > b[-1]:
            res += 1
            a = a[:-1]
            b = b[:-1]
        else:
            a = a[:-1]
            b = b[1:]
    return res

def foo(ifile):
    ifile.readline()
    a = [float(x) for x in ifile.readline().split()]
    b = [float(x) for x in ifile.readline().split()]
    a = sorted(a[:], reverse=True)
    b = sorted(b[:], reverse=True)
    return "%d %d" % (g2(a[:], b[:]), g1(a[:], b[:]))

def main(ifile):
    n = int(ifile.readline().strip())
    for i in range(n):
        print 'Case #%s: %s' % (i+1, foo(ifile))

main(sys.stdin)

