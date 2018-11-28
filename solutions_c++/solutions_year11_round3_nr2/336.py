#include <cstdio>
#include <functional>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

long long a[1123123];
long long dis[1123123];
long long acc[1123123];
long long L, t, N, C;

long long booster(long long i, long long c) {
    if (t > c + 2 * dis[i])
        return 2 * dis[i];
    if (t < c)
        return dis[i];
    return dis[i] + (t-c)/2;
}

int main() {
    int nt, cases = 1;

    scanf(" %d", &nt);
    while (nt--) {
        scanf(" %lld%lld%lld%lld", &L, &t, &N, &C);
        for (int i = 0; i < C; i++)
            scanf(" %lld", &a[i]);
        for (int i = 0; i < C; i++) {
            for (int k = 0; k*C+i+1 <= N; k++)
                dis[k*C+i] = a[i];
            for (int k = -1; k*C+i >= 0; k--)
                dis[k*C+i] = a[i];
        }
        int k = -1;
        acc[0] = 0;
        for (int i = 1; i <= N; i++) {
            acc[i] = acc[i-1] + 2 * dis[i-1];
            if (acc[i] >= t && k == -1) k = i;
        }

        long long res;
        if (k != -1 && L > 0) {
            vector<pair<long long, int> > brd;
            for (int i = k; i < N; i++)
                brd.push_back(make_pair(dis[i], i));

            sort(brd.begin(), brd.end(), greater<pair<long long, int> >());
            vector<bool> selected(N, false);
            for (int i = 0; i < (int)brd.size() && i < L; i++)
                selected[brd[i].second] = true;

            res = 0;
            for (int i = 0; i < k; i++) res += 2 * dis[i];
            for (int i = k; i < N; i++) res += selected[i] ? dis[i] : 2 * dis[i];
            
            // printf("brd.size: %d %d\n", (int)brd.size(), L);

            long long sum = 0;
            for (int i = 0; i < k-1; i++) sum += 2 * dis[i];
            sum += booster(k-1, sum);
            if (L <= (int)brd.size()) selected[brd[L-1].second] = false;
            for (int i = k; i < N; i++) sum += selected[i] ? dis[i] : 2 * dis[i];

            res = min(sum, res);
        } else
            res = acc[N];
            
        // int res = acc[N];
        // if (L > 0)
        //     for (int i = 0; i < N; i++) {
        //         res = min(res,
        //                   acc[i] + booster(i, acc[i]) + acc[N] - acc[i+1]);
        //         if (L > 1)
        //             for (int j = i+1; j < N; j++) {
        //                 int cost = acc[i];
        //                 cost += booster(i, cost);
        //                 cost += acc[j] - acc[i+1];
        //                 cost += booster(j, cost);
        //                 cost += acc[N] - acc[j+1];
        //                 res = min(res, cost);
        //             }
        //     }

        // for (int i = 0; i < N; i++)
        //     printf(" %d", dis[i]);
        printf("Case #%d: %lld\n", cases++, res);
    }

    return 0;
}
