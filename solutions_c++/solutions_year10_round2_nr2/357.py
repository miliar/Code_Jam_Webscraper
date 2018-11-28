#include <cstdio>
#include <cstdlib>
#include <cstring>


int	d[10006],s[10006];
int	n,m,b,t,i,j,k,Ans=0,TEST,T;

int	main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	
	for (scanf("%d",&TEST),T=1;T<=TEST;++T)
	{
		scanf("%d%d%d%d",&n,&m,&b,&t);
		Ans=0;
		for (i=1;i<=n;++i) scanf("%d",&d[i]);
		for (i=1;i<=n;++i) scanf("%d",&s[i]);
		for (j=0,k=0,i=n;i;--i)
		{
			if ((long long)d[i]+s[i]*t>=b)
			{
				++j;
				Ans+=k;
			} else ++k;
			if (j>=m) break;
		}
		printf("Case #%d: ",T);
		if (j>=m) printf("%d\n",Ans); else printf("IMPOSSIBLE\n");
	}
	
	return 0;
}
