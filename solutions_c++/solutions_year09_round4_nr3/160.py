#include <iostream>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
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

int	K;

struct Chart
{
	int	price[100];

	bool operator < (const Chart &c) const
	{
		int	i;

		Fi(K)
		{
			if(price[i] != c.price[i])
				return price[i] < c.price[i];
		}
		return false;
	}
};

Chart	charts[1000];
int	N;

bool g[1000][1000];
int	match[1000];

bool	vis[1000];

bool dfs(int u)
{
	int	v;

	if(vis[u]) return false;
	vis[u] = true;

	for(v = 0; v < N; v++)
	{
		if(g[u][v])
		{
			if(match[v] == -1)
			{
				match[v] = u;
				return true;
			}
			else
			{
				if(dfs(match[v]))
				{
					match[v] = u;
					return true;
				}
			}
		}
	}
	return false;
}


bool intersect(const Chart &c1, const Chart &c2)
{
	int	k;

	Fk(K)
	{
		if(c1.price[k] == c2.price[k]) return true;

		if(k > 0)
		{
			int	d1,d2;

			d1 = c1.price[k] - c2.price[k];
			d2 = c1.price[k-1] - c2.price[k-1];

			if((d1 < 0 && d2 > 0) || (d1 > 0 && d2 < 0))
				return true;
		}
	}
	return false;
}

vector <Chart>	temp;

int main()
{
	int	T,cs;
	int	i,j;

	scanf("%d",&T);

	rab(cs,1,T)
	{
		scanf("%d %d",&N,&K);

		Fi(N) Fj(K) scanf("%d",&charts[i].price[j]);

		sort(charts,charts + N);

		//temp.clear();
		memset(g,0,sizeof(g));

		Fi(N)
		{
			for(j = i + 1; j < N; j++)
				g[i][j] = !intersect(charts[i],charts[j]);
		}

		int	m = 0;

		Fi(N) match[i] = -1;

		Fi(N)
		{
			memset(vis,0,sizeof(vis));

			if(dfs(i)) m++;
		}

		printf("Case #%d: %d\n",cs,N - m);
	}
	return 0;
}
