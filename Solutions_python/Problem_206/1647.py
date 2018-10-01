import sys


def next_catch(K_S, D):
    T = []
    for i in range(len(K_S) - 1):
        # Same speed.
        if K_S[i][1] == K_S[i+1][1]:
            continue

        s1 = K_S[i+1][0] - K_S[i][0]
        t = s1 / K_S[i][1] - K_S[i+1][1]
        if t < 0:
            t = float('inf')

        if not T:
            T.append((i, t))
        while T[-1][0] < i:
            T.append((T[-1][0] + 1, t))

    # Closest horse.
    if K_S[-1][0] < D:
        T.append((len(K_S) - 1, (D - K_S[-1][0]) / K_S[-1][1]))
    return min(T, key=lambda x: x[1])


def solve(K_S, D):
    K_S.sort(key=lambda x: x[0])
    sum_t = 0.0

    while K_S:
        idx, t = next_catch(K_S, D)
        sum_t += t

        new_k_s = []
        for i in range(len(K_S)):
            k = K_S[i][0] + t * K_S[i][1]
            if k >= D:
                continue
            if i == idx and i < len(K_S) - 1:
                v = K_S[i + 1][1]
            else:
                v = K_S[i][1]
            new_k_s.append((k, v))
        K_S = new_k_s

    return D / sum_t


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        src = f.read()

    lines = src.splitlines()
    T = int(lines.pop(0))

    result = ''
    for i in range(T):
        D, N = lines.pop(0).split(maxsplit=1)
        K_S = []
        for j in range(int(N)):
            K, S = lines.pop(0).split(maxsplit=1)
            K_S.append((int(K), int(S)))
        result += 'Case #{idx}: {result}\n'.format(idx=i+1, result=solve(K_S, int(D)))
        #print('Case #{idx}: {result}'.format(idx=i+1, result=solve(K_S, int(D))))

    with open('output.txt', 'w') as f:
        f.write(result)
