#include <cstdio>

using namespace std;

int N, L, H, f[1 << 14];

int go() {
    for (int i = L; i <= H; ++i) {
        for (int j = 0; true; ++j) {
            if (j >= N) return i;
            if (i % f[j] != 0 && f[j] % i != 0) break;
        }
    }

    return -1;
}

int main() {
    int kases;

    scanf("%d", &kases);
    for (int kase = 1; kase <= kases; ++kase) {
        scanf("%d%d%d", &N, &L, &H);
        for (int i = 0; i < N; ++i) scanf("%d", f + i);

        int re = go();

        printf("Case #%d: ", kase);
        if (re < 0) {
            printf("NO\n");
        } else {
            printf("%d\n", re);
        }
    }

    return 0;
}
