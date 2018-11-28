#include <iostream>
using namespace std;
int i,j,n,m,curcase = 1,testcase,ans;
int req[10000];
int G[2000][2000];
void dfs(int l ,int r)
{
	for ( i = l ; i < r ; i++ )
		if (req[i]) break;
	if (i==r) return;
	ans++;
	for ( i = l ; i < r ; i++ )
		if (req[i]) req[i]--;
	if (r-l>2)
	{
		dfs(l,(l+r)/2);
		dfs((l+r)/2,r);
	}
}
int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	for ( scanf("%d",&testcase) ; curcase <= testcase ; curcase++ )
	{
		scanf("%d",&n);
		for ( i = 0 ; i < ( 1 << n) ; i++ )
		{
			scanf("%d",&req[i]);
			req[i] = n-req[i];
		}
		for ( i = n-1 ; i >= 0 ; i-- )
			for ( j = 0 ; j < (1 << i) ; j++ )
				scanf("%d",&G[i][j]);
		ans = 0;
		dfs(0,(1 << n));
		printf("Case #%d: %d\n",curcase,ans);
	}
}
