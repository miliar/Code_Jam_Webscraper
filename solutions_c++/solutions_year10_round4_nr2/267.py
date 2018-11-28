#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
long long W[15][1035][1035],F[15][1035][1035];
int N,cnt[1035];
inline void Update(long long &u,long long v)
{
	if (v<u)	u=v;
}
inline long long dfs(int dep,int k,int l,int r)
{
	if (F[k][l][r]>=0)	return F[k][l][r];
	F[k][l][r]=1LL<<30;
	if (dep==1)
	{
		if (k>=cnt[l]&&k>=cnt[r])	F[k][l][r]=0;
		else
		if (k>=cnt[l]-1&&k>=cnt[r]-1)	F[k][l][r]=W[dep][l][r];
		return F[k][l][r];
	}
	int mid=(l+r)>>1;
	Update(F[k][l][r],dfs(dep-1,k,l,mid)+dfs(dep-1,k,mid+1,r));
	Update(F[k][l][r],dfs(dep-1,k+1,l,mid)+dfs(dep-1,k+1,mid+1,r)+W[dep][l][r]);
	return F[k][l][r];
}
int main()
{
	int T;
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	for (int Te=1;Te<=T;++Te)
	{
		scanf("%d",&N);
		for (int i=1;i<=1<<N;++i)
			scanf("%d",&cnt[i]),cnt[i]=N-cnt[i];
		for (int i=1;i<=N;++i)
		for (int j=1;j<=1<<N;j+=(1<<i))
			scanf("%I64d",&W[i][j][j+(1<<i)-1]);
		memset(F,-1,sizeof(F));
		printf("Case #%d: %I64d\n",Te,dfs(N,0,1,1<<N));
	}
	return 0;
}
