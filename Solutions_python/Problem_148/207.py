from collections import Counter


def main(t):
    N, X = [int(x) for x in raw_input().split()]
    f = Counter(int(x) for x in raw_input().split())
    kk = sorted(f.keys())
    ans = 0
    for k in kk:
        while f[k] > 0:
            f[k] -= 1
            for k2 in range(X-k, 0, -1):
                if f[k2] > 0:
                    f[k2] -= 1
                    break
            ans += 1
    print 'Case #{}:'.format(t+1),
    print ans


if __name__ == '__main__':
    T = input()
    for t in range(T):
        main(t)

