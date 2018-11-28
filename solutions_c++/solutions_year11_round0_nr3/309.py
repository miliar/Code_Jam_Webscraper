#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <queue>
using namespace std;
int dp[2000005][2];
int lg=2000001;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int ca;
    scanf("%d",&ca);
    for(int pp=1; pp<=ca; pp++)
    {
        printf("Case #%d: ",pp);
        int n;
        int c[1024];
        scanf("%d",&n);
        int k=0;
        int mx=lg;
        int tot=0;
        for(int i=0; i<n; i++)
        {
            scanf("%d",&c[i]);
            tot+=c[i];
            mx=min(mx,c[i]);
            k^=c[i];
        }
        if(k!=0)
        {
            puts("NO");
            continue;
        }
        printf("%d\n",tot-mx);
    }
    return 0;
}
