#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cassert>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef long double ld;

#define MAXN 10024

int n, l, c;
int a[MAXN];
int d[MAXN];
ll t;

ll testa(int a)
{
    ll ans = 0;

    for (int i = 0; i < n; ++i)
    {
        if (a != i)
        {
            ans += 2 * d[i];
            continue;
        }

        if (ans >= t)
        {
            ans += d[i];
        }
        else if (t - ans < 2 * d[i])
        {
            ans += d[i] + (t - ans) / 2;
        }
        else
        {
            ans += 2 * d[i];
        }

        //printf ("%d %d: %lld\n", i, d[i], ans);
    }

    return ans;
}

ll testa(int a, int b)
{
    ll ans = 0;

    for (int i = 0; i < n; ++i)
    {
        if (i != a && i != b)
        {
            ans += 2 * d[i];
            continue;
        }

        if (ans >= t)
        {
            ans += d[i];
        }
        else if (t - ans < 2 * d[i])
        {
            ans += d[i] + (t - ans) / 2;
        }
        else
        {
            ans += 2 * d[i];
        }
    }

    return ans;
}

int main (void)
{
    int cases;

    scanf ("%d", &cases);

    for (int caso = 1; caso <= cases; ++caso)
    {
        printf ("Case #%d: ", caso);

        scanf ("%d %lld %d %d", &l, &t, &n, &c);

        for (int i = 0; i < c; ++i)
        {
            scanf ("%d", &a[i]);
        }

        for (int k = 0; k*c <= n; ++k)
        {
            for (int i = 0; i < c; ++i)
            {
                d[k*c + i] = a[i];
            }
        }

        ll ans = testa(-10);

        if (l == 2)
        {
            for (int i = 0; i < n; ++i)
            {
                for (int j = i + 1; j <= n; ++j)
                {
                    ans = min(ans, testa(i, j));
                }
            }
        }
        else if (l == 1)
        {
            for (int i = 0; i < n; ++i)
            {
                ans = min(ans, testa(i));
            }
        }

        printf ("%lld\n", ans);
    }

    return 0;
}

