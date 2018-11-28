#include <cstdio>
using namespace std;

int main(void)
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	bool flag;
	short cls[1001][1001];
	int i,j,k,M,N,T,temp;
	scanf("%d",&T);
	for(int t = 1; t <= T; ++t)
	{
		flag = false;
		scanf("%d",&N);
		for(i=0; i<N; i++)
		{
			for(j=0; j<N; j++)
			{
				cls[i][j] = 0;
			}
		}
		for(i=0; i<N; i++)
		{
			scanf("%d",&M);
			for(j=0; j<M; j++)
			{
				scanf("%d",&temp);
				cls[i][temp-1] = 1;
			}
		}
		for(i=0; !flag && i<N; i++)
		{
			for(j=0; !flag && j<N; j++)
			{
				if(cls[i][j])
				{
					for(k=0; k<N; k++)
					{
						if(cls[k][i]) cls[k][j]++;
						if(cls[k][j]>1)
						{
							flag = true;
							break;
						}
					}
				}
			}
		}
		/*
		for(i=0; i<N; i++)
		{
			for(j=0; j<N; j++)
			{
				if(cls[i][j]>1)
					flag = true;
			}
		}
		*/
		printf("Case #%d: %s\n",t,(flag?"Yes":"No"));
	}
	return 0;
}
