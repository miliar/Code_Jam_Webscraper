#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
using namespace std;

const long maxn = 3010;
const long maxp = 20;
const long INF = 1000000000;

long mi[maxn];
long cost[maxn][maxn];
long f[maxp][maxn][maxp];
long n;

void init()
{
	scanf("%ld", &n);
	for (long i = 1 ; i <= (1 << n); ++i)
	{
		 scanf("%ld", &mi[i]);
		 mi[i] = n - mi[i];
	}
	
	for (long i = n-1; i >= 0; --i)
		for (long j = 1; j <= (1 << i); ++j) scanf("%ld", &cost[i][j]);
}

void solve()
{
	for (long i = 0; i <= n; ++i)
		for (long j = 1; j < maxn; ++j)
			for (long l = 0; l < maxp; ++l) f[i][j][l] = INF;
			
	for (long i = 1; i <= (1 << n); ++i) f[n][i][mi[i]] = 0;
	
	for (long i = n-1; i >= 0; --i)
	{
		for (long tot, j = 1; j <= (1 << i); ++j)
			for (long l1 = 0; l1 <= n; ++l1)
			for (long l2 = 0; l2 <= n; ++l2)
			if (f[i+1][j*2-1][l1] < INF && f[i+1][j*2][l2] < INF)
			{
				tot = max(l1, l2);
				f[i][j][tot] = min(f[i][j][tot], f[i+1][j*2-1][l1] + f[i+1][j*2][l2]);
				
				if (tot > 0)
				f[i][j][tot-1] = min(f[i][j][tot-1], f[i+1][j*2-1][l1] + f[i+1][j*2][l2] + cost[i][j]);
			}
	}
	
	printf("%ld\n", f[0][1][0]);
}

int main()
{
	freopen("BL.in", "r", stdin);
	freopen("BL.out", "w", stdout);
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

