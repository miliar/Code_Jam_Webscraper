#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<list>
#include<queue>
#include<map>
#include<algorithm>
using namespace std;

int csK, csN;
int N, P, M[1024], C[1024], dp[1024][10], mn[1024];

inline int getAns(int p, int k)
{
	if(dp[p][k] >= 0) return dp[p][k];
	if((p<<1) >= N)
	{
		dp[p][k] = (k < mn[p]) ? 0 : C[p];
		return dp[p][k];
	}
	dp[p][k] = getAns(p<<1, k) + getAns((p<<1)+1, k) + C[p];
	if(k < mn[p])
		dp[p][k] = min(dp[p][k], getAns(p<<1, k+1)+getAns((p<<1)+1, k+1));
	return dp[p][k];
}

int main()
{
	int i, j, k, m, t;
	scanf("%d", &csN);
	for(csK = 1; csK <= csN; ++csK)
	{
		scanf("%d", &P);
		N = 1 << P;
		for(i = 0; i < N; ++i)
			scanf("%d", &M[i]);
		for(i = N>>1; i > 0; i >>= 1)
			for(j = i; j < i+i; ++j)
				scanf("%d", &C[j]);
		for(i = N>>1; i < N; ++i)
			mn[i] = min(M[(i<<1)-N], M[(i<<1)-N+1]);
		for(i = (N>>1)-1; i > 0; --i)
			mn[i] = min(mn[i<<1], mn[(i<<1)+1]);
		memset(dp, -1, sizeof(dp));
		printf("Case #%d: %d\n", csK, getAns(1, 0));
	}
}

