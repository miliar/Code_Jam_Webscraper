#include <cstdio>
#include <cassert>

#include <vector>
#include <queue>

using namespace std;

typedef vector<int> TIntVector;
typedef priority_queue< int, vector<int>, greater<int> > THeap;

__int64 cache[200][200];
__int64 sum[200][200];

__int64 Stupido(const TIntVector& counts, int left, int right) {
    if (cache[left][right] == -1) {
        if (left > right) {
            cache[left][right] = 0;
            sum[left][right] = 0;
        } else if (left == right) {
            cache[left][right] = 0;
            sum[left][right] = counts[left];
        } else {
            __int64 best = 123456789012345LL;
            for (size_t i = left; i < right; ++i) {
                __int64 cur = Stupido(counts, left, i) + Stupido(counts, i + 1, right);
                cur += sum[left][i] + sum[i + 1][right];
                if (cur < best)
                    best = cur;
            }
            cache[left][right] = best;
            sum[left][right] = sum[left][left] + sum[left + 1][right];
        }
    }

    return cache[left][right];
}

int main() {
    freopen("input.txt", "r", stdin);
    // freopen("C-small-attempt2.in", "r", stdin); freopen("C-small-attempt2.out", "w", stdout);
    freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);

    int nT;
    scanf("%d", &nT);
    for (int t = 0; t < nT; ++t) {
        memset(cache, -1, sizeof(cache));
        memset(sum, -1, sizeof(sum));

        int n, q;
        scanf("%d%d", &n, &q);
        TIntVector cells(n + 1, 0);
        for (int i = 0; i < q; ++i) {
            int cell;
            scanf("%d", &cell);
            int old = cells[cell];
            while ((cell <= n) && (cells[cell] == old)) {
                cells[cell] = i + 1;
                ++cell;
            }
        }

        {
            TIntVector counts(q + 1, 0);
            for (size_t i = 0; i <= n; ++i)
                ++counts[cells[i]];

            __int64 res = Stupido(counts, 0, counts.size() - 1);

            printf("Case #%d: %I64d\n", t + 1, res - 2*q);
        }
    }

    return 0;
}
