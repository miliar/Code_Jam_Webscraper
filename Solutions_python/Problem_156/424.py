panckakes = []
plates = 0
m = 0

def test_h(h):
    global panckakes
    global m
    t = h
    for p in panckakes:
        t += (p - 1) / h
        if m < t:
            return
    m = t

def solve():
    global panckakes
    global m
    h = max(panckakes)
    m = h
    while h >= 2:
        test_h(h)
        h -= 1
    return m

if __name__ == '__main__':
    f = open('input')
    n = int(f.readline().rstrip())

    for case in range(n):
        plates = int(f.readline().rstrip())
        panckakes = [int(x) for x in f.readline().rstrip().split()]
        print('Case #{0}: {1}'.format(case + 1, solve()))
