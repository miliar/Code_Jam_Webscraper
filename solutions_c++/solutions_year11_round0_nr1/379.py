#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

#define ABS(x)   ( (x) > 0 ? (x) : -(x) )

int     ans, x[2], v[2];
int     tc, n, y, r;
char    s[10000];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int t=1; t<=tc; ++t)
    {
        scanf("%i", &n);
        ans = 0;
        x[0] = x[1] = 1;
        v[0] = v[1] = 0;
        for(int i=0; i<n; ++i)
        {
            scanf("%s %i", s, &y);
            if (s[0] == 'O') r = 0; else r = 1;
            ans  = max(ABS(x[r] - y) + 1 + v[r], ans + 1);
            x[r] = y;
            v[r] = ans;
            //printf("s=%s y=%i  r=%i  v[0]=%i v[1]=%i x[0]=%i x[1]=%i ans=%i\n", s, y, r, v[0], v[1], x[0], x[1], ans);
        }
        printf("Case #%i: %i\n", t, ans);
        
    }
    return 0;
}