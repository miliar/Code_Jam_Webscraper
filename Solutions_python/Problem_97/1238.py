def getRecycle(x):
    a = str(x)
    n = len(a)
    return set(filter(lambda a:a>x, [int(''.join([a[i - j] for i in range(n)])) for j in range(n)]))

def countRecycle(a, b):
    count = 0
    for i in range(a, b+1):
        for j in getRecycle(i):
            if j <= b:
                count += 1
    return count

if __name__ == '__main__':
    import sys
    infile = sys.argv[1]
    f = open(infile)
    T = int(f.readline().strip())
    for i in range(T):
        ln = f.readline().strip().split()
        A, B = map(int, ln)
        print 'Case #%d: %d'%(i+1, countRecycle(A,B))

