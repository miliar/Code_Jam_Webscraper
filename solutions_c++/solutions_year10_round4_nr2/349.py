#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#define REP(i,n) for (int i = 0; i < (n); ++i)
#define FORE(i,c) for (typeof(c.begin()) i = c.begin(); i != c.end(); ++i)
using namespace std;

int T, P;
int M[2000];
long long price[20][2000];
long long dp[20][2000][20];
const long long oo = 999999999999LL;

long long DP(int i, int j, int k)
{
	if (i == 0)
		return M[j]+k >= P ? 0 : oo;
	
	long long& ref = dp[i][j][k];
	if (ref == -1)
	{
		// buy it
		ref = price[i][j] + DP(i-1, 2*j, k+1) + DP(i-1, 2*j+1, k+1);
		// don't buy it
		ref = min(ref, DP(i-1, 2*j, k) + DP(i-1, 2*j+1, k));
		ref = min(ref, oo);
	}
	return ref;
}

int main()
{
	//freopen("B-small-attempt0.in", "r", stdin), freopen("B-small.out", "w", stdout);
	freopen("B-large.in", "r", stdin), freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	REP(t, T)
	{
		scanf("%d", &P);
		REP(i, 1<<P) scanf("%d", &M[i]);
		for (int i = 1; i <= P; i++) REP(j, 1<<(P-i)) scanf("%lld", &price[i][j]);
		memset(dp, -1, sizeof dp);
		printf("Case #%d: %lld\n", t+1, DP(P, 0, 0));
	}
}
