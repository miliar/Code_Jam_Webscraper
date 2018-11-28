#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int R, k, n;
int list[1024];
int next[1024];
long long gain[1024];

void init()
{
    scanf("%d%d%d", &R, &k, &n);
    for (int i = 0; i < n; i ++)
    {
        scanf("%d", list + i);
    }
}

void solve()
{
    long long ans = 0;

    int i, j;
    for (i = 0; i < n; i ++)
    {
        long long tot = 0;
        for (j = 0; j < n; j ++)
        {
            if (tot + list[(i + j) % n] > k) break;
            tot += list[(i + j) % n];
        }
        next[i] = (i + j) % n;
        gain[i] = tot;
    }

    int p = 0;
    while (R --)
    {
        ans += gain[p];
        p = next[p];
    }

//    printf("%I64d\n", ans);
    cout << ans << endl;
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int T, t;
    scanf("%d", &T);

    for (t = 1; t <= T; t ++)
    {
        cout << "Case #" << t << ": ";

        init();
        solve();
    }

    return 0;
}
