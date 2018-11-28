#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

const long maxn = 110;
const long maxm = 310;
const long inf = 1000000000;

long f[maxn][maxm];
long num[maxn];
long n, m, cd, ci, t;


void init()
{
	scanf("%ld%ld%ld%ld", &cd, &ci, &m, &n);
	
	for (long i = 1; i <= n; ++i) 
		scanf("%ld", &num[i]);
}

long min(long x, long y)
{
	return x < y ? x : y;
}

long ab(long x)
{
	return x < 0 ? -x : x;
}

void solve()
{
	for (long i = 0; i <= n; ++i)
		for (long j = 0; j <= 256; ++j) f[i][j] = inf;
		
	f[0][256] = 0;
	
	for (long i = 1; i <= n; ++i)
	{
			//D
			for (long l = 0; l <= 256; ++l)
				if (f[i-1][l] < inf)
					f[i][l] = f[i-1][l] + cd;
			//I
			for (long det, cost, l = 0; l <= 255; ++l)
				for (long j = 0; j <= 256; ++j)
					if (f[i-1][j] < inf)
					{	
						cost = ab(l - num[i]);
						if (j != 256)
						{
							if (m == 0)
							{
								if (l != j) continue;
							}
							else
							{
								det = ab(l - j)-m;
								if (det < 0) det = 0;
								det = det/m + (det%m ? 1 : 0);
								cost += det*ci;
							}
						}

						f[i][l] = min(f[i][l], f[i-1][j] + cost);
					}
/*
			//C
			for (long l = 0; l <= 255; ++l)
				for (long j = 0; j <= 256; ++j)
					if (f[i-1][j] < inf && (ab(l-j)<= m || j == 256))
						f[i][l] = min(f[i][l], f[i-1][j] + ab(l - num[i]) );
*/
	}
	
	long ans = inf;
	for (long i = 0; i <= 256; ++i)
		ans = min(ans, f[n][i]);
	
	printf("%ld\n", ans);
}

int main()
{
	freopen("BL.in", "r", stdin);
	freopen("BL.out", "w", stdout);
	scanf("%ld", &t);
	for (long l = 1; l <= t; ++l)
	{
		init();
		printf("Case #%ld: ", l);
		solve();
	}
	return 0;
}

