import sys

def war(a, b):
    n = k = 0
    for v in a:
        for i, r in enumerate(b[:]):
            if r > v:
                k += 1
                b.pop(i)
                break
        else:
            n += 1
            b.pop(0)
    return n


def dwar(a, b):
    if len(a) == 1:
        return int(a[0] > b[0])
    n = k = 0
    while b:
        x, y = a[-1], b[-1]
        if x > y:
            a.pop()
            b.pop()
            n += 1
        else:
            a.pop(0)
            b.pop()
            k += 1
    return n

if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        _ = sys.stdin.readline()
        a = sorted(map(float, sys.stdin.readline().split()))
        b = sorted(map(float, sys.stdin.readline().split()))
        print('Case #{}: {} {}'.format(i + 1, dwar(a[:], b[:]), war(a, b)))
