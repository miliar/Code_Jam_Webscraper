#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char **argv)
{

	int N, cases, T, n;
	long R, K, G[1001], rnd, tot, totmoney ;

	int i;

    freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-attempt0.out","wt",stdout);

	//freopen("C-large.in","rt",stdin);
	//freopen("C-large.out","wt",stdout);

	scanf("%d",&cases);

	for(T=1; T<=cases; T++)
	{
		scanf("%d %d %d",&R,&K,&N);

		for(n=0; n<N; n++)
			scanf("%d",&G[n]);

		totmoney=0; rnd =0; i=0; 
		while(rnd<R)
		{
			n=0; tot=0;
			while(K >= tot+G[i])
			{
				tot = tot +G[i];

				i++;
				if(i>=N) i=0;

				n++;
				if(n>=N) break;
			}
			rnd++;
			totmoney += tot;
		}

		printf("Case #%d: %d\n",T,totmoney);
	}
	return 0;
}

