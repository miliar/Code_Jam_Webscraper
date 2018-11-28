#include <stdio.h>
#include <iostream>

using namespace std;

int t;
int n, c[1024];

void solve()
{
    int xorAll = 0;
    int sum = 0, mn = 1000010;
    scanf("%d",&n);
    for(int i = 1; i <= n; i ++)
    {
        scanf("%d",&c[i]);
        xorAll ^= c[i];
        sum += c[i];
        mn = min(mn, c[i]);
    }

    if(xorAll) printf("NO\n");
    else printf("%d\n",sum - mn);
}

int main()
{
    scanf("%d",&t);
    for(int i = 1; i <= t; i ++)
    {
        printf("Case #%d: ",i);
        solve();
    }

    return 0;
}
