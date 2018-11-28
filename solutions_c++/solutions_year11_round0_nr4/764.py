#include <cstdio>

using namespace std;

int N, p[1 << 10];

int go() {
    int re = 0;

    for (int i = 0; i < N; ++i) {
        if (p[i] > 0 && p[i] - 1 != i) {
            int j = i;

            do {
                int t = p[j] - 1;

                p[j] = 0;
                j = t;
                ++re;
            } while (j != i);
        }
    }

    return re;
}

int main() {
    int kases;

    scanf("%d", &kases);
    for (int k = 1; k <= kases; ++k) {
        scanf("%d", &N);
        for (int i = 0; i < N; ++i) scanf("%d", p + i);

        printf("Case #%d: %d\n", k, go());
    }

    return 0;
}
