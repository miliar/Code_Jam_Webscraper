#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 128;

int D[N];
long long L, P, C;

void read() {
    scanf("%lld %lld %lld", &L, &P, &C);
}

void pre_proc() {
    D[0] = D[1] = D[2] = 0;
    for (int i = 3; i <= N; ++i) {
        D[i] = 0x3f3f3f3f;
        for (int j = 2; j < i; ++j)
            D[i] = min(D[i], 1 + max(D[j], D[i - j + 1]));
    }
}

void solve() {
    int cnt = 1;
    while (L < P) {
        ++cnt;
        L *= C;
    }
    printf("%d\n", D[cnt]);
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    pre_proc();

    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        read();
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}
