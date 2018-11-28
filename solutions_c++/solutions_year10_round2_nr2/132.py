#include <cstdio>

#include <vector>
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int nT;
    scanf("%d", &nT);
    for (int it = 0; it < nT; ++it) {
        int n, k, b, t;
        scanf("%d%d%d%d", &n, &k, &b, &t);
        typedef vector<int> TIntVector;
        TIntVector x, v;
        for (size_t i = 0; i < n; ++i) {
            int dummy;
            scanf("%d", &dummy);
            x.push_back(dummy);
        }
        for (size_t i = 0; i < n; ++i) {
            int dummy;
            scanf("%d", &dummy);
            v.push_back(dummy);
        }
        TIntVector reach;
        int count = 0;
        for (size_t i = 0; i < n; ++i) {
            reach.push_back(x[i] + v[i]*t >= b);
            if (reach[i])
                count += 1;
        }
        if (count < k) {
            printf("Case #%d: IMPOSSIBLE\n", it + 1);
        } else {
            int swaps = 0;
            int index = n - 1;
            int zeroes = 0;
            while (k > 0) {
                if (reach[index]) {
                    --k;
                    swaps += zeroes;
                } else {
                    ++zeroes;
                }
                --index;
            }
            printf("Case #%d: %d\n", it + 1, swaps);
        }
    }

    return 0;
}
