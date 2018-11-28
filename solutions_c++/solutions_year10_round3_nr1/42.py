#include <cstdio>

#define MAX_N 1024

int N;
int A[MAX_N], B[MAX_N];

void read() {
    scanf("%d", &N);
    for (int i = 1; i <= N; ++i)
        scanf("%d %d", &A[i], &B[i]);
}

void solve() {
    int sol = 0;
    for (int i = 1; i <= N; ++i)
        for (int j = i + 1; j <= N; ++j)
            if ((A[i] < A[j] && B[i] > B[j]) || (A[i] > A[j] && B[i] < B[j]))
                ++sol;
    printf("%d\n", sol);
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        read();
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}
