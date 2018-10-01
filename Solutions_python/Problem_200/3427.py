def tidy(n):
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
    return True


def lt(n):
    n = list(map(int, list(str(n))))
    i = len(n) - 1

    while not tidy(n):
        lw(n, i)
        i -= 1
    n = list(map(str, n))
    return int(''.join(n))

def lw(n, i):
    a = n[i - 1]
    n[i - 1] = a - 1
    n[i] = 9


with open('large.txt') as f:
    f.readline()
    for i, line in enumerate(f):
        n = int(line.strip())
        print('case #{}: {}'.format(i+1, lt(n)))
