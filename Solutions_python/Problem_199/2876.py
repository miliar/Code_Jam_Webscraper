import fileinput


def solve(s, k):
    i = 0
    f = 0
    while i < len(s) - k:
        while s[i] == '+' and i < len(s) - k:
            i += 1
        if s[i] == '-' and i < len(s) - k:
            for j in range(i, i + k):
                s[j] = '+' if s[j] == '-' else '-'
            i += 1
            f += 1
    if s[i:] == ['+'] * k:
        return f
    elif s[i:] == ['-'] * k:
        return f + 1
    else:
        return 'IMPOSSIBLE'


if __name__ == '__main__':
    stdin = fileinput.input()
    nprobs = int(next(stdin).strip())
    for n in range(1, nprobs + 1):
        S, K = next(stdin).strip().split()
        print("Case #%d:" % n, solve(list(S), int(K)))
