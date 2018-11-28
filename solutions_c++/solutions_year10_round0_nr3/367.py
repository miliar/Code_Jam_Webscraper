#include <cstdio>

#include <queue>
#include <vector>

using namespace std;

typedef vector<int> TIntVector;

int main() {
    int nc;
    scanf("%d", &nc);
    for (int c = 1; c <= nc; ++c) {
        int r, k, n;
        scanf("%d%d%d", &r, &k, &n);
        TIntVector g(n);
        for (size_t i = 0; i < n; ++i)
            scanf("%d", &g[i]);
        for (size_t i = 0; i < n; ++i)
            g.push_back(g[i]);
        TIntVector state(n);
        TIntVector cost(n);
        for (size_t i = 0; i < n; ++i) {
            cost[i] = 0;
            size_t j;
            for (j = 0; (j < n) && (cost[i] + g[i + j] <= k); ++j)
                cost[i] += g[i + j];
            state[i] = (i + j) % n;
        }
        long long int result = 0;
        int cstate = 0;
        for (size_t i = 0; i < r; ++i) {
            result += cost[cstate];
            cstate = state[cstate];
        }
        printf("Case #%d: %lld\n", c, result);
    }

    return 0;
}
