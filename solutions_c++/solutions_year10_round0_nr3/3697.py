#include <cstdio>

int	Num[2000];
long long	Ans;
int	m,k,n,Left,Now,T,t,Sum,ans;

inline int Next(int p)
{
	p++;
	if (p>n)	p=1;
	return p;
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		scanf("%d%d%d",&m,&k,&n);
		Sum=0;
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&Num[i]);
			Sum+=Num[i];
		}
		Ans=Now=0;
		for (int i=1;i<=m;i++)
		{
			ans=0;
			Left=k;
			while (Num[Next(Now)]<=Left)
			{
				Now=Next(Now);
				ans+=Num[Now];
				Left-=Num[Now];
			}
			if (ans>Sum)	Ans+=Sum;
			else			Ans+=ans;
		}
		
		printf("Case #%d: %d\n",t,Ans);
	}
}
