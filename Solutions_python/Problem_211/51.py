import time

##import sys
##sys.setrecursionlimit(10002)
INFILE = 'cs.in'
OUTFILE = 'c.out'


def solve(n,k,px,u):
    if u>=n-sum(px):
        return 1.0
    px.sort()
    for i in range(1,n):
        if u<px[i]*i-sum(px[:i]):
            break
    else:
        i=n
    px[:i]=[(u+sum(px[:i]))/i]*i
    print px
    ans=reduce(lambda x,y:x*y,px,1)
    return ans


def read_input(fi):
    read = lambda type: type(fi.readline()[:-1])
    readArray = lambda type: map(type, fi.readline().split())
    readMatrix = lambda type, x: [map(type, fi.readline().split()) for i in range(x)]
    readLines = lambda type, x: [type(fi.readline()[:-1]) for i in range(x)]
    n,k = readArray(int)
    u=read(float)
    px=readArray(float)
    return n,k,px,u


def main():
    fi = file(INFILE)
    fo = file(OUTFILE, 'w')
    time0 = time.time()
    t = int(fi.readline())
    for ti in range(t):
        time1 = time.time()
        ans = "Case #%d: %s" % (ti + 1, solve(*read_input(fi)))
        print ans, "%.3f" % (time.time() - time1)
        fo.write(ans + '\n')
    print "%.3f" % (time.time() - time0)
    fi.close()
    fo.close()


if __name__ == '__main__':
    main()
