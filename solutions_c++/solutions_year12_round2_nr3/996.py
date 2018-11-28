#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define maxk 2000010
#define maxn 500
int dp[maxk];
int sum;
int T,n,cs;
int s[maxn];
int flag[maxn];
int ans1[maxn];
int ans2[maxn];
void output(int k1,int k2)
{
    int cc = 0;
    int t1,t2,i;
    memset(flag,0,sizeof(flag));
    while(k1 != 0)
    {
        if(k1 % 2 == 1)
        {
            flag[cc] = 1;
        }
        cc++;
        k1  = k1 >> 1;
    }
    cc = 0;
    t1 = t2 = 0;
    while(k2 != 0)
    {
        if(k2 % 2 == 1)
        {
            if(flag[cc] == 0)
                ans1[t1++] = s[cc];
            else
                flag[cc] = 0;
        }
        cc++;
        k2 = k2 >> 1;
    }
    for(i = 0; i < n; i++)
    {
        if(flag[i] == 1)
            ans2[t2++] = s[i];
    }
    printf("%d",ans1[0]);
    for(i = 1; i < t1; i++)
        printf(" %d",ans1[i]);
    printf("\n");
    printf("%d",ans2[0]);
    for(i = 1; i < t2; i++)
        printf(" %d",ans2[i]);
    printf("\n");
    return;
}
bool solve()
{
    int i,j;
    //printf("%d\n",sum);
    for(i = 0; i < n; i++)
    {
        for(j = sum; j - s[i] >= 0 ; j--)
        {
            if(dp[j - s[i]]!=-1)
            {
                if(dp[j]==-1)
                {
                    dp[j] = dp[j - s[i]] + (1 << i);
                }
                else
                {
                    output(dp[j],dp[j-s[i]] + (1 << i));
                    return true;
                }
            }
        }
    }
    return false;
}
int main()
{
 freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int i,j;
    while(scanf("%d",&T)!=EOF)
    {
        cs = 1;
        while(T--)
        {
            sum = 0;
            scanf("%d",&n);
            for(i = 0; i < n; i++)
            {
                scanf("%d",&s[i]);
                sum += s[i];
            }
            memset(dp,-1,sizeof(dp));
            dp[0] = 0;
            printf("Case #%d:\n",cs++);
            if(!solve())
                printf("Impossible\n");
        }
    }
    return 0;
}
