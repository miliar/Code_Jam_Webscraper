#include <cstdio>
#include <cstring>

using namespace std;

int     n, tc, x, ans;

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int t=1; t<=tc; ++t)
    {
        scanf("%i", &n);    
        ans = 0;
        for(int i=1; i<=n; ++i) 
        {
            scanf("%i", &x);
            if (x != i) ans++;
        }

        printf("Case #%i: %i.000000\n", t, ans);        
    }
}