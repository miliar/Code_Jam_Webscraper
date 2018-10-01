import sys

def rl():
    return sys.stdin.readline().strip()

def main():
    T = int(rl())
    for i in range(1, T+1):
        C, F, X = map(float, rl().split())
        r = 2.0
        t = 0
        m = X / r + t
        while True:
            t += C / r
            r += F
            n = X / r + t
            if n < m:
                m = n
            else:
                break
        print 'Case #%d: %.7f' % (i, m)

if __name__ == '__main__':
    main()
