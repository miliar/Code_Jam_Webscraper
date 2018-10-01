tens = [1 for i in range(20)]
for i in range(1, 20):
    tens[i] = 10 * tens[i-1]

def solve2():
    def digit(n, i):
        return (n % tens[i+1]) // tens[i]
    n = int(input())
    l = len(str(n))
    for i in range(l):
        di = digit(n, i)
        dip = digit(n, i+1)
        if di < dip:
            n -= (di + 1)*tens[i]
    return n

def solve():
    n = list(reversed(list(int(c) for c in input())))
    for i in range(len(n)-1):
        if n[i] < n[i+1]:
            for j in range(i+1):
                n[j] = 9
            if n[i+1] == 0:
                t = 1
                while n[i+t] == 0:
                    n[i+t] = 9
                    t += 1
                n[i+t] -= 1
            else:
                n[i+1] -= 1
    return ''.join(str(d) for d in reversed(n))

T = int(input())
for t in range(1, T + 1):
    print('Case #%d:' % t, str(int(solve())))

