# -*- coding: utf-8 -*-

def solution(d, k, s):
    length = len(k)
    result = 0
    for i in range(length):
        speed = d / ((d - k[i]) / s[i])
        if i == 0:
            result = speed
        else:
            result = min(speed, result)

    return result

if __name__ == '__main__':
    import sys

    in_path = sys.argv[1]
    with open(in_path, 'r') as f:
        t = int(f.readline().strip())
        results = [0 for _ in range(t)]
        for j in range(t):
            d, n = f.readline().strip().split(' ')
            d = int(d)
            n = int(n)
            kl = [0 for _ in range(n)]
            sl = [0 for _ in range(n)]
            for i in range(n):
                k, s = f.readline().strip().split(' ')
                kl[i] = int(k)
                sl[i] = int(s)

            result = solution(d, kl, sl)
            results[j] = '%.6f' % result

    out_path = sys.argv[2]
    with open(out_path, 'w') as out_f:
        for i in range(t):
            s = 'Case #' + str(i + 1) + ': ' + str(results[i]) + '\n'
            out_f.write(s)
