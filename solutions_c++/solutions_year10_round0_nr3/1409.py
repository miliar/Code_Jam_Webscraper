#include <cstdio>
#define MAXN (1 << 11)
using namespace std;
typedef long long ll;

int t, brt;
ll sol, r, k, n, a[MAXN], next[MAXN], add[MAXN], wh;

int main ()
{
    scanf ("%d", &t);

    while ( t-- )
    {
        scanf ("%lld%lld%lld", &r, &k, &n);
        for (int i=0; i < n; ++i)
            scanf ("%lld", &a[i]);

        for (int i=0; i < n; ++i)
            a[i+n] = a[i];

        for (int i=0; i < n; ++i)
        {
            add[i] = 0;
            for (int j=0; j < n; ++j)
            {
                if (add[i] + a[i+j] > k) { next[i] = (i+j)%n; goto skip; }
                add[i] += a[i+j];
            }
            next[i] = i;
            skip:;
        }
        wh = sol = 0;
        for (int step=0; step < r; ++step)
        {
            sol += add[wh];
            wh = next[wh];
        }
        printf ("Case #%d: %lld\n", ++brt, sol);
    }
    return 0;
}
