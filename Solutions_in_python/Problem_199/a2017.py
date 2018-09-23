import sys


def solve(S, K):
    return iterate(S, K, 0)


def iterate(S, K, N):
    if len(S) == 0 or '-' not in S:
        return N
    if S[0] == '+':
        return iterate(S.lstrip('+'), K, N)
    if len(S) < K:
        return 'IMPOSSIBLE'
    return iterate(''.join(['-' if c == '+' else '+' for c in S[: K]]) + S[K:], K, N + 1)


def main(fn):
    with open(fn, 'r') as fi:
        with open(fn + '.out', 'w') as fo:
            T = int(next(fi).strip())
            for t in range(1, T + 1):
                S, K = next(fi).strip().split()
                ans = solve(S, int(K))
                fo.write('Case #%d: %s\n' % (t, ans))


if __name__ == '__main__':
    main(sys.argv[1])
