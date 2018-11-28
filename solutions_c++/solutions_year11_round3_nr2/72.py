#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <functional>
using namespace std;

typedef long long LL;

#define rep(i, n) for (int i = 0; i < n; i++)
#define sz(v) (int) ((v).size())

int L, N, C;
LL t;
int a[1100000];

int main()
{
//    freopen("../DefaultProject/1.txt", "r", stdin);
    freopen("../DefaultProject/B-large.in", "r", stdin);
    freopen("../DefaultProject/B-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    rep(tc, T)
    {
        printf("Case #%d: ", tc + 1);

        scanf("%d%lld%d%d", &L, &t, &N, &C);
        rep(i, C)
        {
            scanf("%d", &a[i]);
        }
        for (int i = C; i < N; i++)
        {
            a[i] = a[i % C];
        }

        LL ans = 0;
        rep(i, N) ans += a[i];
        ans *= 2;

        int i = 0;
        while (i < N && t > 2 * a[i])
        {
            t -= 2 * a[i];
            i++;
        }
        if (i < N && L > 0)
        {
            vector<LL> benefits;
            for (int j = i + 1; j < N; j++)
                benefits.push_back(a[j]);

            LL ost = a[i] - t / 2;
            benefits.push_back(ost);

            sort(benefits.begin(), benefits.end(), greater<LL>());
            int cnt = min(L, sz(benefits));
            rep(j, cnt)
            {
                ans -= benefits[j];
            }
        }

        printf("%lld\n", ans);
    }

    return 0;
}
