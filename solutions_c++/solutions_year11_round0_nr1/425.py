#include <cstdio>
#include <cstring>
#include <cmath>

int t,n,p[110],i,tempo,tempb;
int o,b,ans,oo,bb;
char ch[110];

void solve()
{
	int i;
	oo=bb=0;
	for (i=0;i<n;i++)
	{
		if (ch[i]=='O')
		{
			if (oo<abs(p[i]-o))
			{
				ans+=abs(p[i]-o)-oo+1;
				bb+=abs(p[i]-o)-oo+1;
			}
			else
			{
				ans+=1;
				bb+=1;
			}
			oo=0;
			o=p[i];
		}
		else 
		{
			if (bb<abs(p[i]-b))
			{
				ans+=abs(p[i]-b)-bb+1;
				oo+=abs(p[i]-b)-bb+1;
			}
			else
			{
				ans+=1;
				oo+=1;
			}
			b=p[i];
			bb=0;
		}
	}
}
int main()
{
	freopen("A-large.in","r",stdin);freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (int id=1;id<=t;id++)
	{
		scanf("%d",&n);
		tempo=tempb=1;
		for (i=0;i<n;i++)
		{
			scanf(" %c %d",&ch[i],&p[i]);
		}
		ans=0;o=b=1;
		solve();
		printf("Case #%d: %d\n",id,ans);
	}
	return 0;
}