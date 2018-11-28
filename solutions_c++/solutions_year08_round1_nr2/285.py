#include <stdio.h>
int favor[2000][2000];
int N,M;
void solve()
{
	int q,w,e,ans=-1,at;
	for (q=0;q<(1<<N);q++)
	{
		int c=0;
		for (w=0;w<N;w++) if (q&(1<<w)) c++;
		for (w=0;w<M;w++)
		{
			for (e=0;e<N;e++)
				if (favor[w][e]>=0)
				{
					int t=!!(q&(1<<e));
					if (t==favor[w][e]) break;
				}
			if (e>=N) break;
		}
		if (w>=M) 
			if (ans<0 || ans>c)
			{
				ans=c;
				at=q;
			}
	}
	if (ans<0) printf(" IMPOSSIBLE\n");
	else
	{
		for (q=0;q<N;q++)
			printf(" %d",!!(at&(1<<q)));
		printf("\n");
	}
}
int main()
{
	int t,T;
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		scanf("%d",&N);
		scanf("%d",&M);
		int q,w;
		for (q=0;q<M;q++)
			for (w=0;w<N;w++)
				favor[q][w]=-1;//no idea
		for (q=0;q<M;q++)
		{
			int a,b,z;
			scanf("%d",&z);
			for (w=0;w<z;w++)
			{
				scanf("%d %d",&a,&b);
				favor[q][a-1]=b;
			}
		}
		printf("Case #%d:",t);
		solve();	
	}
	return 0;
}
