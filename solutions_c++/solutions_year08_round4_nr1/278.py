#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

#define	MAX_NODE	20000
#define INF		100000000

int 	ntype[MAX_NODE];
int	value[MAX_NODE];
int 	chtype[MAX_NODE];
int	nodes;

int 	min_change[MAX_NODE][2];

int memo(int u,int v)
{
	if(2 * u > nodes) return (value[u - 1] == v) ? 0 : INF;

	int &res = min_change[u - 1][v];

	if(res >= 0) return res;

	int	l[2],r[2];
	int	i,j,c;

	res = INF;

	l[0] = memo(2 * u,0);
	l[1] = memo(2 * u,1);
	r[0] = memo(2 * u + 1,0);
	r[1] = memo(2 * u + 1,1);

	for(i = 0; i <= 1; i++)
	{
		for(j = 0; j <= 1; j++)
		{
			if((i & j) == v)
			{
				c = l[i] + r[j];
				if(ntype[u-1] != 1)
				{
					if(chtype[u-1] == 0)
						c = INF;
					else
						c++;
				}

				res = min(res,c);
			}

			if((i | j) == v)
			{
				c = l[i] + r[j];

				if(ntype[u-1] != 0)
				{
					if(chtype[u-1] == 0)
						c = INF;
					else
						c++;
				}

				res = min(res,c);
			}

			//if(u == 1) printf("i=%d, j=%d, res=%d,c = %d, v = %d\n",i,j,res,c,v);
		}
	}

	//printf("%d %d: %d\n",u,v,res);

	return res;	
}

int main()
{
	int	N,cs;
	int	i;
	int	V;

	scanf("%d",&N);

	for(cs = 1; cs <= N; cs++)
	{
		scanf("%d %d",&nodes,&V);

		for(i = 0; i < (nodes - 1) / 2; i++)
			scanf("%d %d",&ntype[i],&chtype[i]);
			

		for(; i < nodes; i++)
			scanf("%d",&value[i]);

		memset(min_change,-1,sizeof(min_change));

		printf("Case #%d: ",cs);

		int k = memo(1,V);

		if(k >= INF)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",k);
	}
	
	return 0;
}
