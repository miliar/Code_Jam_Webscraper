#include <stdio.h>
#include <algorithm>

using namespace std;

#define MAXN                1000000

int A[MAXN];
int S[MAXN];

long long solve()
{
    int L, N, C;
    int i, j;
    long long elapsed, t, dt;

    scanf("%d %lld %d %d", &L, &t, &N, &C);

    for (i = 0; i < C; i++)
        scanf("%d", A + i);

    elapsed = 0;
    for (i = 0; i < N; i++) {
        dt = A[i % C] * 2;
        if (elapsed >= t)
            S[i] = dt / 2;
        else if (elapsed + dt <= t)
            S[i] = 0;
        else
            S[i] = (elapsed + dt - t) / 2;
        elapsed += dt;
    }

    sort(S, S + N);

    for (i = 0; i < L; i++)
        elapsed -= S[N - 1 - i];

    return elapsed;
}

int main()
{
    int i, T;

    scanf("%d", &T);

    for (i = 1; i <= T; i++)
        printf("Case #%d: %lld\n", i, solve());

    return 0;
}
