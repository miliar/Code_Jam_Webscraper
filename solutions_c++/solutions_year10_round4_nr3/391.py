#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
using namespace std;

const long maxn = 210;

long g[maxn][maxn];
long n, m;

void init()
{
	long r;
	scanf("%ld", &r);
	
	memset(g, 0, sizeof(g));
	
	long x1, x2, y1, y2;
	
	n = 0; m = 0;
	for (long i = 1; i <= r; ++i)
	{
		scanf("%ld%ld%ld%ld", &x1, &y1, &x2, &y2);
		
		n = max(n, y2);
		m = max(m, x2);
		for (long i = y1; i <= y2; ++i)
			for (long j = x1; j <= x2; ++j) g[i][j] = 1;
	}
}

void solve()
{
	long step = 0;
	for (long tot = 1; tot > 0;)
	{
		tot = 0;
		++step;
		for (long i = n; i >= 1; --i)
			for (long j = m; j >= 1; --j)
			{
				if (g[i][j]) 
				{
					if ((i > 1 && g[i-1][j] == 1) || (j > 1 && g[i][j-1] == 1))
					{
						++tot;
						 continue;
					}
					g[i][j] = 0;
				}
				else 
				{
					if ((i > 1 && g[i-1][j] == 1) && (j > 1 && g[i][j-1] == 1))
					{
						++tot;
						g[i][j] = 1;
					}
				}
				
			}
/*
	for (long i = 1; i <= n; ++i) 
	{
		for (long j = 1; j <= m; ++j) printf("%ld", g[i][j]);
		printf("\n");
	}
	printf("\n");
*/
	}
	
	printf("%ld\n", step);
}


int main()
{
	freopen("CS.in", "r", stdin);
	freopen("CS.out", "w", stdout);
	
	long t;
	scanf("%ld", &t);
	for (long l = 1; l <= t; ++l)
	{
		init();
		
		printf("Case #%ld: ", l);
		solve();
	}
	return 0;
}

