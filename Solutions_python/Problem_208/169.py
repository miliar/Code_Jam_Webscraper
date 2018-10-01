
def pony_express(N, cities, M, Q):
    assert len(Q) == 1 and Q[0] == (1, N)
    assert all(M[i][j] == -1 for i in range(N) for j in range(N) if j != i + 1)

    D = [M[i][i + 1] for i in range(N - 1)]
    S = [0]
    for d in D:
        S.append(S[-1] + d)
    T = [None] * N
    T[0] = 0
    for i in range(N - 1):
        max_distance, speed = cities[i]
        for j in range(i + 1, N):
            distance = S[j] - S[i]
            if distance > max_distance:
                break
            t = T[i] + distance / speed
            if T[j] is None or T[j] > t:
                T[j] = t
    return T[-1]

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, Q = map(int, input().split())
        L = [tuple(map(int, input().split())) for i in range(N)]
        M = [tuple(map(int, input().split())) for i in range(N)]
        Q = [tuple(map(int, input().split())) for i in range(Q)]
        result = pony_express(N, L, M, Q)
        print("Case #{}: {}".format(i + 1, result))
