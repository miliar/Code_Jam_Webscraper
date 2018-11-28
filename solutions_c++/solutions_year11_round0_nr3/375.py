#include <cstdio>

using namespace std;

int tc, n, x;
int sum, sumx, lmin;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int t=1; t<=tc; ++t)
    {
        scanf("%i", &n);
        sum = sumx = 0;
        lmin = 1000000000;
        for(int i=0; i<n; ++i)
        {
            scanf("%i", &x);
            sumx = sumx ^ x;
            sum += x;
            if (x < lmin) lmin = x;
        }
        if (sumx)
            printf("Case #%i: NO\n", t);
        else
            printf("Case #%i: %i\n", t, sum - lmin);
    }
}