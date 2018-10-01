import numpy as np


def main():
    t = int(input())
    for case in range(1, t + 1):
        n, k = map(int, input().split())
        u = float(input())
        ps = sorted(list(map(float, input().split())))

        while u > 0.:
            m, i, mx = min(ps), 0, max(ps)
            if np.isclose(m, mx):
                for j in range(n):
                    ps[j] += u / n
                break
            while i < n and np.isclose(ps[i], m):
                i += 1
            d = i * (ps[i] - ps[0])
            if d < u:
                for j in range(i):
                    ps[j] = ps[i]
                u -= d
            else:
                for j in range(i):
                    ps[j] += u / i
                break

        print('Case #{}: {}'.format(case, np.prod(ps)))


if __name__ == '__main__':
    main()
