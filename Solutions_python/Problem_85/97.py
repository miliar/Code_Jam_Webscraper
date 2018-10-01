import sys

def solve(input):
    T = int(input.readline())
    for ti in xrange(1, T+1):
        line = input.readline().split()
        L = int(line[0])
        t = int(line[1])
        N = int(line[2])
        C = int(line[3])
        a = []
        for c in xrange(C):
            a.append(int(line[4+c]))
        hour = 0
        L1 = -1
        L2 = -1
        Ldist = 0
        for n in xrange(N - 1):
            distance = a[n % C]
            hour += distance * 2
            if t <= hour:
                L1 = n
                if t < hour:
                    L2 = n
                    Ldist = (hour - t) / 2
                break
        Lbuild = [0] * N
        if L1 >= 0:
            b = a[:]
            while L > 0:
                if len(b) == 0:
                    break
                maxb = max(b)
                b.remove(maxb)
                for n in xrange(N-2, L1-1, -1):
                    if a[n % C] == maxb:
                        if n == L2:
                            nextmaxb = max(b)
                            if nextmaxb < Ldist:
                                Lbuild[n] = 1
                                L -= 1
                        else:
                            Lbuild[n] = 1
                            L -= 1
                    if L == 0:
                        break
        hour = 0
        for n in xrange(N):
            distance = a[n % C]
            if Lbuild[n] and t <= hour:
                hour += distance
            elif Lbuild[n] and hour < t < hour + distance * 2:
                hour += (distance - (t - hour) / 2) + (t - hour)
            else:
                hour += distance * 2
        print "Case #%d:" % ti, hour

if __name__ == '__main__':
    solve(sys.stdin)