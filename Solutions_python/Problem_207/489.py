gr = {
    'R': {'Y', 'B', 'G'},
    'B': {'Y', 'R', 'O'},
    'Y': {'R', 'B', 'V'},
    'V': {'Y'},
    'O': {'B'},
    'G': {'R'}
}


def solve_small(r, y, b):
    sol = ''
    if r > 0 and y > 0:
        m = min(r, y)
        sol = 'RY' * m
        r -= m
        y -= m
    elif r > 0 and b > 0:
        m = min(r, b)
        sol = 'RB' * m
        r -= m
        b -= m
    elif y > 0 and b > 0:
        m = min(y, b)
        sol = 'YB' * m
        y -= m
        b -= m

    choices = {'R': r, 'Y': y, 'B': b}

    sol = list(sol)
    impossible = False
    while not impossible:
        impossible = True
        nsol = []
        for i in range(len(sol)):
            nsol.append(sol[i])
            u = gr[sol[i]] & gr[sol[(i+1)%len(sol)]]
            for e in u:
                if choices[e] > 0:
                    nsol.append(e)
                    choices[e] -= 1
                    impossible = False
                    break
        sol = nsol
        del nsol
    return ''.join(sol) if all(c == 0 for _, c in choices.items()) else 'IMPOSSIBLE'


t = int(input())
for case in range(1, t + 1):
    N, r, o, y, g, b, v = list(map(int, input().split()))
    # choices = {'R': r, 'O': o, 'Y': y, 'G': g, 'B': b, 'V': v}
    print('Case #{}: {}'.format(case, solve_small(r, y, b)))
