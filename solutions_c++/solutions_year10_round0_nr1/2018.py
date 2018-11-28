#include <cstdio>

using namespace std;

int main() {
    int T; scanf("%d", &T);
    for (int c = 1; c <= T; c++) {
        int N, K; scanf("%d%d", &N, &K);
        int V = (1 << N) - 1;
        printf("Case #%d: %s\n", c, ((V & K) == V) ? "ON" : "OFF");
    }
    return 0;
}
