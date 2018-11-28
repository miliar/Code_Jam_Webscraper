#include <cstdio>

using namespace std;

int cost[101][256];
int color[101];
int t, D, I, M, N;

int calc(int a, int b)
{
	int c=a-b;
	if (c<0)
		c=-c;
	if (c<=M)
		return 0;
	return (c-1)/M;
}
int calc2(int a, int b)
{
	int c=a-b;
	if (c<0)
		c=-c;
	if (c==0)
		return 0;
	return 1+(c-1)/M;
}

int ABS(int a, int b)
{
	int c=a-b;
	return c<0?-c:c;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for (int cases=1;cases<=t;cases++)
	{
		scanf("%d%d%d%d", &D, &I, &M, &N);
		for (int i=0;i<N;i++)
			scanf("%d", &color[i]);
		for (int i=0;i<N;i++)
		{
			for (int j=0;j<=255;j++)
			{
				cost[i][j] = 10000000;
				//use i elment
				{
					if (M==0)
					{
						int res=0;
						if (i>0)
							res=ABS(color[i],j)+cost[i-1][j];
						else
							res=ABS(color[i],j);
						if (cost[i][j]>res)
							cost[i][j]=res;
					}
					else
					{
						for (int k=0;k<=255;k++)
						{
							int res =0;
							if (i>0)
								res=cost[i-1][k]+I*(calc(k,color[i])+calc2(color[i],j));
							else
								res=I*calc2(color[i],j);
							if (cost[i][j]>res)
								cost[i][j]=res;
							res=0;
							if (i>0)
								res=cost[i-1][k]+ I*calc(k,j) +ABS(color[i],j);
							else
								res=ABS(color[i],j);
							if (cost[i][j]>res)
								cost[i][j]=res;
						}
					}
				}
				//not use i
				{
					int res;
					if(i>0)
						res=cost[i-1][j]+D;
					else
						res=D;
					if (cost[i][j]>res)
						cost[i][j]=res;
				}
			}
		}
		int ans=1000000;
		for (int i=0;i<=255;i++)
			if (cost[N-1][i]<ans)
				ans=cost[N-1][i];
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}