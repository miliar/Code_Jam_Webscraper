#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <queue>
#include <bitset>
#include <sstream>
using namespace std;

#define	rep(i,N)	for((i) = 0; (i) < (N); (i)++)
#define	rab(i,a,b)	for((i) = (a); (i) <= (b); (i)++)
#define	Fi(N)		rep(i,N)
#define	Fj(N)		rep(j,N)
#define	Fk(N)		rep(k,N)
#define	sz(v)		(int)v.size()

const int debug_flag	 = 0;

#define	DBG(f,x)	if(debug_flag & f) x

bool	g[1000][1000];

bool	gs[1000][1000];

int main()
{
	int	T,cs;
	int	N,M;
	int	u,v;
	int	i,j;
	int	perm[1000];

	scanf("%d",&T);

	rab(cs,1,T)
	{
		scanf("%d",&N);

		memset(g,0,sizeof(g));
		
		Fi(N-1)
		{
			scanf("%d %d",&u,&v);
			g[u-1][v-1] = g[v-1][u-1] = true;
		}

		scanf("%d",&M);

		memset(gs,0,sizeof(gs));

		Fi(M-1)
		{
			scanf("%d %d",&u,&v);
			gs[u-1][v-1] = gs[v-1][u-1] = true;
		}

		Fi(N) perm[i] = i;

		bool flag = false;

		do
		{
			Fi(M) 
			{
				Fj(M)
				{
					u = perm[i];
					v = perm[j];

					if(gs[i][j] != g[u][v])
						break;
				}

				if(j < M) break;
			}
			if(i >= M)
			{
				flag = true;
				break;
			}

		} while(next_permutation(perm,perm + N));

		Fi(M)
		{
			DBG(1,printf("%d ",perm[i]));
		}

		DBG(1,printf("\n"));

		printf("Case #%d: %s\n",cs,flag ? "YES" : "NO");

	}

	return 0;
}
