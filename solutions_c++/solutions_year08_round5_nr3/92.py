#include <iostream>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <map>
#include <functional>
#include <queue>
#include <bitset>
#include <sstream>
#include <vector>
using namespace std;

#define	sz(v)	(int)v.size()
#define	rep(i,n)	for((i)=0;(i) < (n); (i)++)
#define	rab(i,a,b)	for((i)=(a);(i) <= (b); (i)++)
#define	Fi(N)		rep(i,N)
#define	Fj(N)		rep(j,N)
#define	Fk(N)		rep(k,N)

typedef pair<int,int>	pii;

char	b[100][100];
int	M,N;

pii	match[100][100];
bool	visited[100][100];

bool dfs(int r,int c)
{
	int	dr,dc;
	int	nr,nc;

	visited[r][c] = true;

	//printf("%d %d\n",r,c);

	for(dc = -1; dc <= 1; dc += 2)
	{
		rab(dr,-1,1)
		{
			nr = r + dr;
			nc = c + dc;

			if(nr < 0 || nr >= M) continue;
			if(nc < 0 || nc >= N) continue;
			if(b[nr][nc] == 'x') continue;

			if(visited[nr][nc]) continue;
			
			if(match[nr][nc].first == -1)
			{
				match[nr][nc] = pii(r,c);
	//			printf("matched with: %d,%d\n",nr,nc);
				return true;
			}
			else
			{
				pii	o = match[nr][nc];

				visited[nr][nc] = true;

				if(dfs(o.first,o.second))
				{
					match[nr][nc] = pii(r,c);
					return true;
				}
			}
		}
	}

	return false;
}

int main()
{
	int	T,cs;
	int	i,j;
	int	nodes;

	scanf("%d",&T);

	rab(cs,1,T)
	{
		scanf("%d %d",&M,&N);

		nodes = 0;

		Fi(M)
		{
			scanf("%s",b[i]);

			Fj(N) if(b[i][j] != 'x') nodes++;
		}

		int	m = 0;

		Fi(M) Fj(N) match[i][j] = pii(-1,-1);

		for(j = 0; j < N; j += 2)
		{
			
			Fi(M)
			{
				if(b[i][j] == 'x') continue;
				memset(visited,0,sizeof(visited));


				if(dfs(i,j)) 
				{
	//				printf("matched with: (%d,%d)\n",i,j);
					m++;
				}
			}
		}

		printf("Case #%d: %d\n",cs,max(nodes - m,m));
	}
	return 0;
}
