#include<stdio.h>

int A, N, M;

int main(void)
{
	int T, l0;

	int x1, y1, x2, y2;


	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d %d",&N,&M,&A);

		for(x1=0;x1<=N;x1++)
		{
			for(y2=0;y2<=M;y2++)
			{

				// ..
				for(x2=0;x2<=N;x2++)
				{
					for(y1=0;y1<=M;y1++)
					{
						if(x1 * y2 - y1 * x2 == A)
						{
							goto maki;
						}
					}
				}
			}
		}

		printf("Case #%d: IMPOSSIBLE\n",l0);
		continue;
maki:
		printf("Case #%d: 0 0 %d %d %d %d\n",l0,x1,y1,x2,y2);
	}
}