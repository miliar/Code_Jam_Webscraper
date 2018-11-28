#include <cstdio>

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        unsigned int N, K;
        scanf("%u%u", &N, &K);
        bool on = (K & ((1 << N) - 1)) == ((1 << N) - 1);
        printf("Case #%d: %s\n", i, on ? "ON" : "OFF");
    }
}
