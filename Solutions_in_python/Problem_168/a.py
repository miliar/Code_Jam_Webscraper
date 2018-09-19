import math

__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"


test = int(input())


def print_m(m):
    return
    print()
    for r in m:
        print(''.join([str(v) for v in r]))


def generate_m(x, y, value):
    m = []
    for i in range(y):
        m2 = []
        for j in range(x):
            m2.append(value)
        m.append(m2)
    return m


def next(a, b, d):
    if d == '^':
        return a, b - 1
    if d == '<':
        return a - 1, b
    if d == '>':
        return a + 1, b
    if d == 'v':
        return a, b + 1


def walk(a, b, d=None):
    if d is not None:
        how_i_walk[b][a] = d
    if working[b][a]:
        return False
    working[b][a] = True
    if m[b][a] == '.':
        new_a, new_b = next(a, b, d)
    else:
        new_a, new_b = next(a, b, m[b][a])
        d = m[b][a]
    if new_a < 0 or new_a >= x or new_b < 0 or new_b >= y:
        return True
    return walk(new_a, new_b, d)


def merge(target, source):
    for i in range(x):
        for j in range(y):
            if source[j][i]:
                target[j][i] += 1
    return target


def get_max():
    max_v = 0
    m_i, m_j = -1, -1
    for i in range(x):
        for j in range(y):
            if m[j][i] != '.' and not changed[j][i] and counting[j][i] > max_v:
                max_v = counting[j][i]
                m_i = i
                m_j = j
    return m_i, m_j


def check_done():
    for i in range(x):
        for j in range(y):
            if counting[j][i] > 0:
                return False
    return True


def find_direction(a, b):
    # >
    for t in range(a+1, x):
        if m[b][t] != '.':
            return '>'
    # <
    for t in range(0, a):
        if m[b][t] != '.':
            return '<'
    # ^
    for t in range(0, b):
        if m[t][a] != '.':
            return '^'
    # v
    for t in range(b+1, y):
        if m[t][a] != '.':
            return 'v'


for t in range(1, test+1):
    print("Case #" + str(t) + ": ", end="")

    y, x = [int(v) for v in input().split(' ')]

    m = []
    for j in range(y):
        m.append([v for v in input()])

    print_m(m)

    step = 0

    changed = generate_m(x, y, False)

    while True:

        processed_arrow = generate_m(x, y, False)

        counting = generate_m(x, y, 0)
        how_i_walk = generate_m(x, y, '.')

        for i in range(x):
            for j in range(y):
                if m[j][i] != '.' and not processed_arrow[j][i]:
                    working = generate_m(x, y, False)
                    success = walk(i, j)
                    if success:
                        counting = merge(counting, working)

        print_m(counting)

        if not check_done():
            step += 1
            i, j = get_max()
            changed[j][i] = True
            if i < 0:
                print('IMPOSSIBLE')
                break
            new_d = find_direction(i, j)
            if new_d is None:
                print('IMPOSSIBLE')
                break
            m[j][i] = new_d
            print_m(m)
        else:
            print(step)
            break


