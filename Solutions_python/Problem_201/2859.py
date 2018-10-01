

from collections import deque

T = int(raw_input())


def check(n):
    b = 10
    while n:
        d = n % 10
        if d <= b:
            b = d
        else:
            return False
        n = n // 10
    return True


def foo(n, k):
    sl = [-1] + [0 for _ in range(n)] + [-1]
    pos = {}

    best = None
    for i in range(1, k+1):
        best = None
        for s in range(len(sl)):
            if sl[s]:
                continue
            c = s - 1
            l, r = 0, 0
            while c >= 0:
                if not sl[c]:
                    l += 1
                else:
                    break
                c -= 1
            c = s + 1
            while c < len(sl):
                if not sl[c]:
                    r += 1
                else:
                    break
                c += 1
            mn = min(l, r)
            mx = max(l, r)
            if not best or mn > best[0]:
                best = (mn, s, mx, l, r)
            elif mn == best[0]:
                if mx > best[2]:
                    best = (mn, s, mx, l, r)
        sl[best[1]] = i
       # print(best)


    return best[2], best[0]
    


for t in range(T):
    line = raw_input()
    line = line.split()
    n, k = int(line[0]), int(line[1])
    a, b = foo(n, k)
    print("Case #{}: {} {}".format(t + 1, a, b))
