#include <stdio.h>
#include <stdlib.h>

int dp[31]={0,1};
void init()
{
    for(int i=2;i!=31;++i) dp[i]=2*dp[i-1]+1;
}
void solve()
{
    int cases,n,k;
    scanf("%d",&cases);
    for(int t=0;t!=cases;++t)
    {
        scanf("%d%d",&n,&k);
        if(k>=dp[n] && (k-dp[n])%(dp[n]+1)==0)
            printf("Case #%d: ON\n",t+1);
        else printf("Case #%d: OFF\n",t+1);
    }
}
int main()
{
    init();
    solve();
    return 0;
}
