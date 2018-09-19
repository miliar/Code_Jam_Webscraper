import sys
import random
import threading
sys.setrecursionlimit(3000)

def bar(a, nx, x):
    return [y-nx for y in a[nx:x]]

def foo2(a, level, height):
    #print a, level, height
    picks = [0]
    i = 0
    n = len(a)
    while True:
        if a[i] == n:
            break
        if a[i] > n:
            return None
        picks.append(a[i])
        i = a[i]
    picks.append(n)

    res = []
    nx = 0
    for x in picks:
        if x == nx:
            res.append(height - level*(n-x))
        else:
            t = foo2(bar(a, nx, x), level+1, height-level*(n-x))
            if t is None:
                return None
            res += t
            #res.append(height - level*(n-x))
        nx = x+1
    return res

def meiju(n):
    if n <= 2:
        yield [1, 0]
        return
    for x in meiju(n-1):
        yield x+[0]
        yield x+[1]
    return

def foo2(a, b, maxi):
    a0 = [0] * (maxi+10)
    for i in range(len(a)):
        if b[i] == 0:
            for x in a[i]:
                a0[x] |= 1
        else:
            for x in a[i]:
                a0[x] |= 2
    return len([x for x in a0 if x == 3])

def convert(a):
    b = {}
    idx = 0
    res = [[] for i in range(len(a))]
    for i, x in enumerate(a):
        for y in x:
            if y not in b:
                b[y] = idx
                idx += 1
            res[i].append(b[y])
    return res, idx


def foo(ifile):
    n = int(ifile.readline())
    a = [set(ifile.readline().split()) for i in range(n)]
    a, maxi = convert(a)

    res = 1000000
    for x in meiju(n):
        res = min(res, foo2(a, x, maxi))
    return res


def main():
    ifile = sys.stdin
    #n = int(ifile.readline())
    n = 1
    for i in range(n):
        sys.stdout.write('%s' % foo(ifile))
        #print 'Case #%d: %s' % (i+1, foo(ifile))
        sys.stdout.flush()


main()

