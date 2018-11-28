#include "stdio.h"
int L,D,N,boo[5001];
char x[5001][16];
int main()
{
	char y;
	int c,i,j,k;
	scanf("%d%d%d",&L,&D,&N);
	for(i=0;i<D;i++)
		scanf("%s",x[i]);
	c=0;
	getchar();
	for(c=1;c<=N;c++)
	{
		for(i=0;i<D;i++)
			boo[i]=0;
		for(i=0;i<L;i++)
		{
			y=getchar();
			if(y=='(')
			{
				while(y=getchar())
				{
					if(y==')')
						break;
					for(k=0;k<D;k++)
						if(y==x[k][i])
							boo[k]++;
				}
			}
			else
				for(k=0;k<D;k++)
					if(y==x[k][i])
						boo[k]++;
		}
		getchar();
		j=0;
		for(i=0;i<D;i++)
			if(boo[i]==L)
				j++;
		printf("Case #%d: %d\n",c,j);
	}
	return 0;
}