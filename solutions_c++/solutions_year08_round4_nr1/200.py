#include<stdio.h>

#define INF 1000000000

int a[100000], b[100000], n, m;
int D[100000][2];

void Go(int root)
{
	int t1, t2;
	int v1, v2;
	if(root <= m) // inter
	{
		t1 = root * 2;
		t2 = root * 2 + 1;
		Go(t1);
		Go(t2);

		D[root][0] = INF;
		D[root][1] = INF;

		if(a[root] == 0) // or
		{
			for(v1=0;v1<=1;v1++)
			{
				for(v2=0;v2<=1;v2++)
				{
					if(D[root][v1 || v2] > D[t1][v1] + D[t2][v2])
					{
						D[root][v1 || v2] = D[t1][v1] + D[t2][v2];
					}
				}
			}
		}
		else
		{
			for(v1=0;v1<=1;v1++)
			{
				for(v2=0;v2<=1;v2++)
				{
					if(D[root][v1 && v2] > D[t1][v1] + D[t2][v2])
					{
						D[root][v1 && v2] = D[t1][v1] + D[t2][v2];
					}
				}
			}
		}

		if(b[root] == 1) // changable
		{
			for(v1=0;v1<=1;v1++)
			{
				for(v2=0;v2<=1;v2++)
				{
					if(D[root][v1 || v2] > D[t1][v1] + D[t2][v2] + 1)
					{
						D[root][v1 || v2] = D[t1][v1] + D[t2][v2] + 1;
					}
				}
			}
			for(v1=0;v1<=1;v1++)
			{
				for(v2=0;v2<=1;v2++)
				{
					if(D[root][v1 && v2] > D[t1][v1] + D[t2][v2] + 1)
					{
						D[root][v1 && v2] = D[t1][v1] + D[t2][v2] + 1;
					}
				}
			}
		}
	}
	else // leaf
	{
		D[root][a[root]] = 0;
		D[root][1 - a[root]] = INF;
	}
}

int main(void)
{
	int T;
	int l0, l1, l2;
	int t1;

	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);

	scanf("%d",&T);

	for(l0=1;l0<=T;l0++)
	{
		scanf("%d %d",&n,&t1);

		m = (n - 1) >> 1;
		for(l1=1;l1<=m;l1++)
		{
			scanf("%d %d",&a[l1],&b[l1]);
		}
		for(l1=m+1;l1<=n;l1++)
		{
			scanf("%d",&a[l1]);
		}

		Go(1);
		if(D[1][t1] == INF) printf("Case #%d: IMPOSSIBLE\n",l0);
		else printf("Case #%d: %d\n",l0,D[1][t1]);

	}
}