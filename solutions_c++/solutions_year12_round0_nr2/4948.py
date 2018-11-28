#include <cstdio>

int main() {
    int ntests;
    std::scanf("%d", &ntests);
    for (int ctest = 1; ctest <= ntests; ctest++) {
        int n, s, p;
        std::scanf("%d%d%d", &n, &s, &p);

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            int c;
            std::scanf("%d", &c);

            if ((c/3) + !!(c%3) >= p)
                cnt++;
            else if (s && c >= 2 && (c/3) + !!(c%3) + 1 >= p && c % 3 != 1) {
                cnt++;
                s--;
            }
        }

        std::printf("Case #%d: %d\n", ctest, cnt);
    }

    return 0;
}
