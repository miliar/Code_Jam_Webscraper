#include <vector>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cstring>
#include <algorithm>
#include <functional>
#include <cstdlib>
#include <cmath>
#include <list>
#include <cctype>
#include <limits>

using namespace std;

typedef __int64 i64;

const int NMAX = 1010;

vector<i64> bo;
i64 d[NMAX];
i64 L, t, N, C;

i64 calc()
{
    i64 now = 0;
    i64 pos = 0;
    for (i64 i = 0; i < L; ++i) {
        if (bo[i] < pos) continue;
        now += 2 * (d[bo[i]] - d[pos]);
        i64 next = d[bo[i] + 1] - d[bo[i]];
        if (now + 2 * next < t) {
            now += 2 * next;
        } else {
            i64 x = max(0LL, t - now);
            now += next + x / 2;
        }
        pos = bo[i] + 1;
    }
    now += 2 * (d[N] - d[pos]);
    return now;
}

i64 brute(i64 id)
{
    if (id == L) {
        return calc();
    }
    i64 res = numeric_limits<i64>::max();
    for (i64 i = 0; i < N; ++i) {
        bo.push_back(i);
        res = min(res, brute(id + 1));
        bo.pop_back();
    }
    return res;
}

void solve()
{
    int tc;
    scanf("%d", &tc);
    for (int tci = 1; tci <= tc; ++tci) {
        scanf("%lld%lld%lld%lld", &L, &t, &N, &C);
        t = t * 2;
        vector<i64> a;
        for (i64 i = 0; i < C; ++i) {
            i64 in;
            scanf("%lld", &in);
            a.push_back(in * 2);
        }
        d[0] = 0;
        for (i64 i = 0; i < N; ++i) {
            d[i + 1] = a[i % C] + d[i];
        }
        bo.clear();
        i64 ans = brute(0) / 2;
        printf("Case #%d: %lld\n", tci, ans);
    }
}

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    solve();
    return 0;
}