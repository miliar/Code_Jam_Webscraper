#include <algorithm>
#include <cstdio>

using namespace std;

int main() {
    int kases;

    scanf("%d", &kases);
    for (int k = 1; k <= kases; ++k) {
        int sean = 0;
        int pat = 0;
        int mi = 1 << 30;
        int n;

        for (scanf("%d", &n); n > 0; --n) {
            int item;

            scanf("%d", &item);

            sean += item;
            pat ^= item;
            mi = min(mi, item);
        }

        printf("Case #%d: ", k);
        if (pat == 0) {
            printf("%d\n", sean - mi);
        } else {
            printf("NO\n");
        }
    }

    return 0;
}
