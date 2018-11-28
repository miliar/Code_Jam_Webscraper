#include <cstdio>
#include <cmath>
#include <cstring>

int t,n;
int queue[1010],ans,flag[1010];

void solve()
{
	int p;
	memset(flag,0,sizeof(flag));
	for (int i=1;i<=n;i++)
		if (flag[i]==0)
	{
		ans--;
		p=i;
		while(flag[p]==0)
		{
			flag[p]=1;
			p=queue[p];
		}
	}
}

void solve1()
{
	for (int i=1;i<=n;i++)
		if (queue[i]==i)ans--;
}

int main()
{
	freopen("D-small-attempt1.in","r",stdin);freopen("d.out","w",stdout);
	scanf("%d",&t);
	for (int id=1;id<=t;id++)
	{
		scanf("%d",&n);
		for (int i=1;i<=n;i++)scanf("%d",&queue[i]);
		ans=n;
		solve1();
		printf("Case #%d: %d\n",id,ans);
	}
	return 0;
}
