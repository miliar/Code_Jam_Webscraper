#include<stdio.h>

int a[1000],N,L,H;

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int Cas=1;Cas<=T;Cas++)
	{
		scanf("%d%d%d",&N,&L,&H);
		for (int i=0;i<N;i++)
			scanf("%d",&a[i]);
		int i,j;
		for (i=L;i<=H;i++)
		{
			for (j=0;j<N;j++)
				if (i%a[j]!=0&&a[j]%i!=0)
					break;
			if (j==N) break;
		}
		printf("Case #%d: ",Cas);
		if (i<=H)
			printf("%d\n",i);
		else
			printf("NO\n");
	}
}