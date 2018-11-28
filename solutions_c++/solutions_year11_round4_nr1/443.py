#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

#define W first
#define L second.first
#define R second.second


const int MAXN = 10000;

pair < long double, pair < long double, long double > > a[MAXN];
long double s, r, t;


long double run(long double l, long double w)
{
    long double f = min(t, l / (r + w));
    t -= f;
    return f + (l - f * (r + w)) / (s + w);
}

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("in", "rt", stdin);
        freopen("out", "wt", stdout);
    #endif

    int ctest;
    scanf("%d", &ctest);
    for (int test = 1; test <= ctest; test++)
    {
        printf("Case #%d: ", test);

        long double x;
        int n;

        cin >> x >> s >> r >> t >> n;
        long double p = 0, ans = 0, d = 0;

        for (int i = 0; i < n; i++)
        {
            cin >> a[i].L >> a[i].R >> a[i].W;
            d += a[i].L - p;
            p = a[i].R;
        }
        d += x - p;
        a[n++] = make_pair(0, make_pair(0, d));

        sort(a, a + n);
        for (int i = 0; i < n; i++)
            ans += run(a[i].R - a[i].L, a[i].W);
        printf("%.9lf\n", (double)ans);
    }

    return 0;
}
