#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdio>

using namespace std;

long long ans,money[1002];
int T,c,r,k,n;
int g[1002],visit[1002];

int next(int p)
{
	if (p==n)
		return 1;
	else
		return p+1;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&c);
	T=0;

	while (c>0)
	{
		T++,c--,ans=0;

		scanf("%d%d%d",&r,&k,&n);
		long long sum=0;
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&g[i]);
			sum+=(long long)g[i];
			money[i]=0,visit[i]=0;
		}

		if (sum<=(long long)k)
		{
			printf("Case #%d: %I64d\n",T,sum*(long long)r);
			continue;
		}

		visit[n]=1;
		int p=n,last=n,L;
		long long Tmoney;
		while (r>0)
		{
			r--;
			long long delta=0;
			while (delta+(long long)g[next(p)]<=(long long)k)
			{
				delta+=(long long)g[next(p)];
				p=next(p);
			}
			ans+=delta;
			if (visit[p]==0)
			{
				visit[p]=visit[last]+1;
				money[p]=money[last]+delta;
				last=p;
			}
			else
			{
				L=visit[last]+1-visit[p];
				Tmoney=money[last]+delta-money[p];
				last=p;
				break;
			}
		}

		ans+=Tmoney*(long long)(r/L);
		r-=(r/L)*L;

		while (r>0)
		{
			r--;
			long long delta=0;
			while (delta+(long long)g[next(p)]<=(long long)k)
			{
				delta+=(long long)g[next(p)];
				p=next(p);
			}
			ans+=delta;
		}

		printf("Case #%d: %I64d\n",T,ans);
	}

	fclose(stdin);fclose(stdout);
	return 0;
}
