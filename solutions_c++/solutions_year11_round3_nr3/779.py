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
#include <algorithm>

using namespace std;

#define MAXN 10008

typedef long long ll;

ll f[MAXN];
int n;
ll l, h;

int main (void)
{
    int cases;

    scanf ("%d", &cases);

    for (int caso = 1; caso <= cases; ++caso)
    {
        scanf ("%d %lld %lld", &n, &l, &h);

        for (int i = 0; i < n; ++i)
        {
            scanf ("%lld", &f[i]);
        } 

        printf ("Case #%d: ", caso);

        bool ok = false;
        for (ll ans = l; ans <= h; ++ans)
        {
            ok = true;

            for (int i = 0; i < n; ++i)
            {
                if (f[i] % ans != 0 && ans % f[i] != 0)
                {
                    ok = false;
                    break;
                }
            }

            if (ok)
            {
                printf ("%lld\n", ans);
                break;
            }
        }

        if (!ok)
        {
            printf ("NO\n");
        }

    }

    return 0;
}

