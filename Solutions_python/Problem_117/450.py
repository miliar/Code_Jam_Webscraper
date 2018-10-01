import sys
from collections import defaultdict

def valid(A, n, m):
    for i in range(n):
        for j in range(m):
            f1, f2 = 0, 0
            for k in range(n):
                if A[k][j]>A[i][j]:
                    f1 = 1
            for k in range(m):
                if A[i][k]>A[i][j]:
                    f2 = 1
            if f1 and f2:
                return False
    return True

if __name__ == '__main__':
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)
    output = open('jamqual2.out', 'w')
    t = int(f.readline())
    for test in xrange(1, t+1):
        str1 = "Case #%d: " %(test)
        output.write(str1)
        n, m = map(int, f.readline().split())
        grid = []
        for i in range(n):
            line = map(int, f.readline().split())
            grid.append(line)
        if valid(grid, n, m):
            output.write('YES'+'\n')
        else:
            output.write('NO'+'\n')
    output.close()
