import sys

def foo(ifile):
    ifile.readline()
    a = [int(x) for x in ifile.readline().split()]
    b = sorted(a)
    n = len(a)
    res = 0
    for x in b:
        i = a.index(x)
        res += min(i, len(a)-i-1)
        a = a[:i] + a[i+1:]
    return res



def main(ifile):
    n = int(ifile.readline().strip())
    for i in range(n):
        print 'Case #%s: %s' % (i+1, foo(ifile))

main(sys.stdin)

