#include<stdio.h>
#include<algorithm>

using namespace std;

const int inf = 1000000000;

int n,v;
int t[20000],c[20000],f[20000][2];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ntest;
	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		scanf("%d%d",&n,&v);
		int i;
		for(i=1;i<=(n-1)/2;i++) scanf("%d%d",&t[i],&c[i]);
		for(;i<=n;i++)
		{
			int x;
			scanf("%d",&x);
			if(x==0) f[i][0]=0,f[i][1]=inf;
			else f[i][0]=inf,f[i][1]=0;
		}
		for(i=(n-1)/2;i>0;i--)
		{
			f[i][0] = f[i][1] = inf;
			if(c[i]==1 || t[i]==0)
			{
				f[i][0] = min(f[i][0], f[i*2][0] + f[i*2+1][0] + (t[i]==1?1:0));
				f[i][1] = min(f[i][1], f[i*2][1] + f[i*2+1][1] + (t[i]==1?1:0));
				f[i][1] = min(f[i][1], f[i*2][1] + f[i*2+1][0] + (t[i]==1?1:0));
				f[i][1] = min(f[i][1], f[i*2][0] + f[i*2+1][1] + (t[i]==1?1:0));
			}
			
			if(c[i]==1 || t[i]==1)
			{
				f[i][0] = min(f[i][0], f[i*2][0] + f[i*2+1][0] + (t[i]==0?1:0));
				f[i][1] = min(f[i][1], f[i*2][1] + f[i*2+1][1] + (t[i]==0?1:0));
				f[i][0] = min(f[i][0], f[i*2][1] + f[i*2+1][0] + (t[i]==0?1:0));
				f[i][0] = min(f[i][0], f[i*2][0] + f[i*2+1][1] + (t[i]==0?1:0));
			}
		}
		if(f[1][v]>inf/2) printf("Case #%d: IMPOSSIBLE\n",test);
		else printf("Case #%d: %d\n",test,f[1][v]);
	}
	return 0;
}
