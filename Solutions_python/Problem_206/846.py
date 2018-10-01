D = 0
N = 0


def main():
    T = int(raw_input().strip())
    global D
    global N
    for case_num in range(T):
        D, N = map(int, raw_input().strip().split(' '))
        k = [None for _ in range(N)]
        s = [None for _ in range(N)]
        for i in range(N):
            k[i], s[i] = map(int, raw_input().strip().split(' '))

        max_time = 0
        for i in range(N):
            t = float((D - k[i])) / s[i]
            if t > max_time:
                max_time = t

        print 'Case #{}: {}'.format(case_num + 1, format(round(D / max_time, 6), '.6f'))


if __name__ == '__main__':
    main()
