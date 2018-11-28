#include <cstdio>

using namespace std;

int main() {
    int t; scanf("%d", &t);
    for (int ncase = 1; ncase <= t; ++ncase) {
        int n, s, p; scanf("%d%d%d", &n, &s, &p);
        int count = 0;
        for (int i = 0; i < n; ++i) {
            int g; scanf("%d", &g);
            if (g >= p) {
                if ((g + 2) / 3 >= p)
                    ++count;
                else if ((g + 4) / 3 >= p && s > 0) {
                    --s;
                    ++count;
                }
            }
        }
        printf("Case #%d: %d\n", ncase, count);
    }
    return 0;
}
