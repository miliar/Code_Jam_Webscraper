#include <algorithm>
using namespace std;
#define N 1010

int g[N];
long long list[N*2];
int next[30][N];
long long dp[30][N];

int main()
{
	int t;
	int r,n;
	long long k;
	int x,y,z;
	long long ans;
	scanf("%d",&t);
	for(z=1;z<=t;++z)
	{
		scanf("%d%I64d%d",&r,&k,&n);
		for(x=0;x<n;++x)
			scanf("%I64d",&list[x]);
		for(x=1;x<n;++x)
			list[x]+=list[x-1];
		for(x=0;x<n;++x)
			list[n+x]=list[n-1]+list[x];
		k=min(k,list[n-1]);
		y=upper_bound(list,list+n+1,k)-list;
		next[0][0]=(y>=n?y-n:y),dp[0][0]=list[y-1];
		for(x=1;x<n;++x)
		{
			for(;y<x+n && list[y]-list[x-1]<=k;++y);
			next[0][x]=(y>=n?y-n:y),dp[0][x]=list[y-1]-list[x-1];
		}
		for(x=1;x<30;++x)
			for(y=0;y<n;++y)
				next[x][y]=next[x-1][next[x-1][y]],dp[x][y]=dp[x-1][y]+dp[x-1][next[x-1][y]];
		for(ans=0,x=0,y=0;r>0 && x<30;++x,r>>=1)
			if(r&1)
				ans+=dp[x][y],y=next[x][y];
		printf("Case #%d: %I64d\n",z,ans);
	}
	scanf(" ");
	return 0;
}
