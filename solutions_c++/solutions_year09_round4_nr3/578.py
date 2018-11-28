#include <cstdio>
#include <cstring>
#include <climits>
#include <ctime>

const int MAX_N = 16;
const int MAX_K = 25 + 5;

inline int min(int a, int b)
{
	return a < b ? a : b;
}

inline int sign(int a)
{
	return a > 0 ? 1 : a == 0 ? 0 : -1;
}

int T;
int N, K;
bool g[MAX_N][MAX_N];
int h[MAX_N][MAX_K];
bool ok[1 << MAX_N];

int dp[1 << MAX_N];
int rec(int mask)
{
	int &ret = dp[mask];
	if(ret != -1)	return ret;
	if(mask == 0)	return ret = 0;
	int res = INT_MAX;
	for(int to = mask; to; to = mask & (to - 1))
		if( ok[to] )
			res = min(res, rec(mask ^ to) + 1);
	return ret = res;
}

int main()
{
	scanf("%d", &T);
	for(int t = 0; t < T; t ++)
	{
		scanf("%d %d", &N, &K);
		for(int i = 0; i < N; i ++)
			for(int j = 0; j < K; j ++)
				scanf("%d", &h[i][j]);
		memset(g, 1, sizeof(g));
		for(int i = 0; i < N; i ++)
			for(int j = 0; j < N; j ++)
			{
				if( h[i][0] == h[j][0] )
				{
					g[i][j] = 0;
					continue;
				}
				for(int ind = 0; ind < K; ind ++)
//					if( (long long)((long long)h[i][ind] - (long long)h[j][ind]) * (long long)((long long)h[i][0] - (long long)h[j][0]) <= 0LL )
					if( sign( h[i][ind] - h[j][ind] ) != sign( h[i][0] - h[j][0] ) )
					{
						g[i][j] = 0;
						break;
					}
			}
		memset(ok, 1, sizeof(ok));
		for(int mask = 0; mask < (1 << N); mask ++)
			for(int i = 0; i < N; i ++)	if( mask & (1 << i) )
				for(int j = 0; j < i; j ++)	if( mask & (1 << j) )
					if( g[i][j] == 0 )
						ok[mask] = 0;
		memset(dp, -1, sizeof(dp));
		printf("Case #%d: %d\n", t + 1, rec((1 << N) - 1));
	}
	fprintf(stderr, "%lf\n", clock() / double(CLOCKS_PER_SEC));
    return 0;
}
