
import sys

def calc_coords(n, A, B, C, D, x0, y0, M):
    P = [(x0, y0)]
    X = x0
    Y = y0
    for i in range(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        P.append((X, Y))
    return P

def try_all(n, A, B, C, D, x0, y0, M):
    P = calc_coords(n, A, B, C, D, x0, y0, M)
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (P[i][0] + P[j][0] + P[k][0]) % 3 == 0:
                    if (P[i][1] + P[j][1] + P[k][1]) % 3 == 0:
                        c += 1
    return c


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: %s <input> <output>" % sys.argv[0]
        sys.exit()
    fd = open(sys.argv[1], 'r')
    fd2 = open(sys.argv[2], 'w')
    n = int(fd.readline())
    for i in xrange(n):
        X = fd.readline().strip().split(' ')
        n, A, B, C, D, x0, y0, M = map(int, X)
        x = try_all(n, A, B, C, D, x0, y0, M)
        fd2.write("Case #%i: %s\n" % (i + 1, x))
    fd.close()
    fd2.close()
