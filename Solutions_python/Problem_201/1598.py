def solve(N, K):
    print(N, K)
    stalls = [0] * N

    def _L_s(S):
        L_s, j = 0, S
        while j >= 0 and stalls[j] < 1:
            L_s, j = L_s + 1, j - 1
        return L_s - 1

    def _R_s(S):
        R_s, j = 0, S
        while j < len(stalls) and stalls[j] < 1:
            R_s, j = R_s + 1, j + 1
        return R_s - 1

    for i in range(1, K + 1):
        L_ss, R_ss = [_L_s(S) for S in range(N)], [_R_s(S) for S in range(N)]
        keyed = [(min(L_s, R_s), max(L_s, R_s), -S) for L_s, R_s, S in zip(L_ss, R_ss, range(N))] 
        choice = sorted(keyed, reverse=True)[0]
        stalls[-choice[2]] = i

    return choice[1], choice[0]

def solve2(N, K):
    from math import floor, log2
    if K == 1:
        X = N
    else:
        this = 2 ** floor(log2(K))
        previous = 2 ** floor(log2(K // 2))
        X = solve2(N, (K % previous) + previous)[K % this >= previous]
    return X // 2, (X - 1) // 2

if __name__ == '__main__':
    for i in range(int(input())):
        print('Case #{}: {} {}'.format(i + 1, *solve2(*list(map(int, input().split())))))
