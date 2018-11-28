#include <cstdio>

void solve(int tcase)
{
    int n;
    scanf("%d", &n);
    int tot = 0, xr = 0, Min = 9999999;
    
    for(int i = 1; i <= n; i++) 
    {
        int tmp;
        scanf("%d", &tmp);
        xr ^= tmp;
        tot += tmp;
        if(Min > tmp) Min = tmp;
    }
    tot -= Min;
    printf("Case #%d: ", tcase);
    if(xr != 0) printf("NO\n");
    else printf("%d\n", tot);
}

int main()
{
    //freopen("C-large2.in", "r", stdin);
    //freopen("C-large2.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++) solve(i);
}
