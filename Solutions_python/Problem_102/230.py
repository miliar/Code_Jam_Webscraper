import os,sys

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for ti in range(T):
        a = map(int, sys.stdin.readline().split(' '))
        n = a[0]
        a.pop(0)
        s = 0
        for i in range(0,n):
            s += a[i]
        avg = s*2 / n
        all_score = s*2
        lows = n
        for i in range(n):
            if a[i] > avg:
                lows -= 1
                all_score -= a[i]
        low_avg = all_score * 1.0 / lows
        r = []
        for i in range(n):
            if a[i] > avg:
                r.append(0.0)
            else:
                r.append((low_avg - a[i] ) / s * 100.0)
        print 'Case #%d: %s' % (ti+1, ' '.join(map(lambda x: '%.6f' % x, r)))


