#include <cstdio>
#include <algorithm>
#define MAXN (1 << 10)
using namespace std;

int t, brt, sol, n, a[MAXN];

inline int abs (int x)
{
    return (x >= 0)? (x):(-x);
}

int main ()
{
    scanf ("%d", &t);

    while ( t-- )
    {
        sol = 0;
        scanf ("%d", &n);
        for (int i=0; i < n; ++i)
            scanf ("%d", &a[i]);
        int gcd = abs (a[1] - a[0]);
        for (int i=0; i < n; ++i)
            for (int j=i+1; j < n; ++j)
                gcd = __gcd (gcd, abs(a[i]-a[j]));
        sol = gcd - (a[0] % gcd);
        if (sol == gcd) sol = 0;
        printf ("Case #%d: %d\n", ++brt, sol);
    }

    return 0;
}
