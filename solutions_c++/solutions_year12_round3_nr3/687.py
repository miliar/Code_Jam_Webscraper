#include <queue>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

long long a[110],aa[110],b[110],bb[110];
long long dp[110][110][110];
int n,m;

long long f(int x,int y,int z)
{
    if(dp[x][y][z]!=-1)
        return dp[x][y][z];
    if(x==n || y==m)
        return dp[x][y][z]=0;

    dp[x][y][z]=0;
    int i,j,k;
    long long qq,ww;
    qq=0;
    for(i=x;i<n;i++)
    {
        if(aa[i]==z)
	qq+=a[i];
        ww=0;
        for(j=y;j<m;j++)
        {
	if(bb[j]==z)
	    ww+=b[j];
	//for(k=1;k<=100;k++)
	    dp[x][y][z]= max(dp[x][y][z],f(i+1,j+1,aa[i+1])+min(ww,qq));
	    dp[x][y][z]= max(dp[x][y][z],f(i+1,j+1,bb[j+1])+min(ww,qq));
        }
    }
    return dp[x][y][z];
}
int main ()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,j;
    int tt,t;
    scanf("%d",&tt);
    for(t=1; t<=tt; t++)
    {
        scanf("%d %d", &n, &m);
        for(i=0; i<n; i++)
        {
	scanf("%lld %lld", &a[i], &aa[i]);
        }
        for(i=0; i<m; i++)
        {
	scanf("%lld %lld", &b[i], &bb[i]);
        }

        memset(dp,-1,sizeof dp);
        long long ans =0;
        for(i=1;i<=100;i++)
        {
	ans=max(ans,f(0,0,i));
        }
        printf("Case #%d: %lld\n", t, ans);
    }
    return 0;
}