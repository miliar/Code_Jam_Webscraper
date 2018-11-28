/*Candy Splitting*/

#include<stdio.h>

int C[15];

int main()
{
	int i,j,k,limit,max,N,num,pcurrentsum,scurrentsum,ptotal,stotal,T;
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C.out","wt",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%d",&N);
		ptotal=stotal=0;
		for(j=0;j<N;j++)
		{
			scanf("%d",&C[j]);
			ptotal^=C[j];
			stotal+=C[j];
		}
		if(ptotal)
		{
			printf("Case #%d: NO\n",i);
			continue;
		}
		limit=1<<N;
		max=0;
		for(j=1;j<limit-1;j++)
		{
			pcurrentsum=scurrentsum=0;
			num=j;
			k=0;
			while(num>0)
			{
				if(num&1)
				{
					pcurrentsum^=C[k];
					scurrentsum+=C[k];
				}
				num>>=1;
				k++;
			}
			if(!(pcurrentsum^(stotal-scurrentsum)))
				if(max<scurrentsum)
					max=scurrentsum;
		}
		printf("Case #%d: %d\n",i,max);
	}
	return 0;
}