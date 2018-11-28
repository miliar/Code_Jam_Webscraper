#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
using namespace std;
int res[30],tt,tim,n,m;
int g[30];
inline void dfs(int p,int w)
{
	if(p>n)
	{
		int i;
		for(i=n;i>1;i=g[i]);
		if(i==1)
			res[n]++;
		return;
	}
	g[p]=0;
	dfs(p+1,w);
	g[p]=w;
	dfs(p+1,w+1);
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&tim);
	for(int i=2;i<=25;i++)
	{
		n=i;
		dfs(2,1);
		res[n]%=100003;
	}
	for(int tt=1;tt<=tim;tt++)
	{
		scanf("%d",&n);
		printf("Case #%d: %d\n",tt,res[n]);
	}
	return 0;
}
