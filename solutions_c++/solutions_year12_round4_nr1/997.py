#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char dp[10000][10001];

int n;
long long dist[10000], vine[10000], D;

int getReach(int ind, long long len)
{
	long long maxDist = dist[ind]+len;
	if(maxDist>=D) return n;
	return upper_bound(dist, dist+n, maxDist) - dist - 1;
}

char getAns(int ind, int reach)
{
//	printf("called: %d %d\n", ind, reach);
	if(ind > reach) return 0;

	char &ret=dp[ind][reach];
	if(ret!=-1) return ret;

	ret=0;
	if(reach==n) ret=1;
	else
	{
		if(getAns(ind, reach-1)) ret=1;
		else
		{
			long long nextLen = dist[reach] - dist[ind];
			nextLen = min(nextLen, vine[reach]);
			if(getAns(reach, getReach(reach, nextLen))) ret=1;
		}
	}

//	printf("%d %d, %d\n", ind, reach, ret);

	return ret;
}

int main(void)
{
	int T;
	scanf("%d", &T);
	for(int caseN=1;caseN<=T;caseN++)
	{
		scanf("%d", &n);
		for(int i=0;i<n;i++) for(int j=0;j<=n;j++) dp[i][j]=-1;
		for(int i=0;i<n;i++)
			scanf("%lld %lld", dist+i, vine+i);
		scanf("%lld", &D);

//		printf("%d\n", n);
		
		printf("Case #%d: %s\n", caseN, getAns(0, getReach(0, dist[0]))?"YES":"NO");
	}

	return 0;
}
