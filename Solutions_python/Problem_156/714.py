def red(k, m, diners):
    j = diners.index(m)
    diners[j] -= k
    diners.append(k)
    return diners

def solve(diners):
    m = max(diners)
    if m == 1:
        return 1
    elif m == 2:
        return 2
    elif m == 3:
        return 3
    if m == 4 and diners.count(m) > 1:
        return 4
    if m/2 <= diners.count(m):
        return m
    din = []
    for i in range(2, m/2+1):
        din.append(red(i, m, list(diners)))
    din = map(solve, din)
    din.append(m-1)
    return 1 + min(din)


def main():
    N = int(raw_input())
    for i in xrange(N):
        n = int(raw_input())
        diners = [int(j) for j in raw_input().split()]
        print 'Case #{0}: {1}'.format(i + 1, solve(diners))


if __name__ == '__main__':
    main()
