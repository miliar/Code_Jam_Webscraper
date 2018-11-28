#include <stdio.h>
#include <stdlib.h>

int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);

	int times;
	scanf("%d",&times);

	int i,j,judge;
	int N,K;
	for (i=1;i<=times;i++)
	{
		scanf("%d %d",&N,&K);

		judge=0;

		for (j=0;j<N;j++)
		{
			judge+=K & 0x01;
			K=K>>1;
		}

		if (judge==N)
		{
			printf("Case #%d: ON\n",i);
		}
		else
		{
			printf("Case #%d: OFF\n",i);
		}
	}

}