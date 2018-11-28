#include <stdio.h>
#include <stdlib.h>

const int T = 100;
const int D = 255;
const int I = 255;
const int M = 255;
const int A = 255;
const int N = 100;

const int MAX = D*I*N;

main()
{
	int t, d, i, m, n;
	int get[N];
	int ans[N+1][A+1+1], min;
	scanf("%d", &t);
	for (int j=1;j<=t;j++)
	{
		scanf("%d%d%d%d", &d, &i, &m, &n);
		for (int k=0;k<n;k++)
			scanf("%d", &get[k]);
		
		for (int k=0;k<=n;k++)
			for (int l=0;l<=A+1;l++)
				ans[k][l]=MAX;
		ans[0][A+1]=0;
		
		for (int k=0;k<n;k++)
			for (int l=0;l<=A+1;l++)
			{
				ans[k+1][l]<?=ans[k][l]+d;
				for (int o=0;o<=A;o++)
				{
					if (l==A+1)
						ans[k+1][o]<?=ans[k][l]+abs(get[k]-o);
					else
					{
						if (o==l)
							ans[k+1][o]<?=ans[k][l]+abs(get[k]-o);
						else if (m!=0)
							ans[k+1][o]<?=ans[k][l]+(abs(o-l)-1)/m*i+abs(get[k]-o);
					}
				}
			}
		
		min=MAX;
		for (int k=0;k<=A+1;k++)
			min<?=ans[n][k];
		
		printf("Case #%d: %d\n", j, min);
	}
}
