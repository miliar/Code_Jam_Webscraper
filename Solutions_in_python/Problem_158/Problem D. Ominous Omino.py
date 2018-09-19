
FIGURES_1 = [
    (1, 1)
]

FIGURES_2 = [
    (1, 2),
]

FIGURES_3 = [
    (2, 2),
    (3, 1)
]

FIGURES_4 = [
    (2, 2),
    (3, 2),
    (3, 3),
    (3, 3),
    (4, 1)
]

FIGURES = {1: FIGURES_1, 2: FIGURES_2, 3: FIGURES_3, 4: FIGURES_4}


def solve(X, R, C):
    if R * C % X != 0:
        return 'RICHARD'

    for fig in FIGURES[X]:
        if (R < fig[0] or C < fig[1]) and (R < fig[1] or C < fig[0]):
            return 'RICHARD'

    return 'GABRIEL'


def main():
    # inp_file = 'input.txt'
    # inp_file = 'D-small-attempt0.in'
    inp_file = 'D-small-attempt1.in'
    with open(inp_file, 'r') as f, open('output.txt', 'w') as f2:
        T = int(f.readline())
        for i in xrange(T):
            case = f.readline().strip()
            X, R, C = map(int, case.split(' '))

            ans = solve(X, R, C)
            ans_s = 'Case #{}: {}\n'.format(i+1, ans)
            f2.write(ans_s)

            print X, R, C
            print ans_s


if __name__ == '__main__':
    main()
