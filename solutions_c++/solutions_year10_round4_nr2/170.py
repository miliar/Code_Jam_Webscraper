#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int dp[10000][12];
int n;
int c[10000];
int m[1100];
int p2[12];

const int INF = 1000000000;

int go(int pos, int ile){
	if(dp[pos][ile] != -1) return dp[pos][ile];
	if(pos >= p2[n]){
		if(ile + m[pos-p2[n]] >= n) dp[pos][ile] = 0;
		else dp[pos][ile] = INF;
		return dp[pos][ile];
	}
	dp[pos][ile] = min(go(2*pos,ile+1) + go(2*pos+1,ile+1) + c[pos], go(2*pos,ile) + go(2*pos+1,ile));
	dp[pos][ile] = min(dp[pos][ile],INF);
	return dp[pos][ile];
}

int main()
{
	p2[0] = 1;
	for(int i=1; i<12; ++i) p2[i] = 2*p2[i-1];
	int cases;
	scanf("%d", &cases);
	for(int iii=1; iii<=cases; ++iii){
		scanf("%d", &n);
		for(int i=0; i<p2[n]; ++i) scanf("%d", &m[i]);
		for(int poz=n-1; poz>=0; --poz){
			for(int i=p2[poz]; i<p2[poz+1]; ++i) scanf("%d", &c[i]);
		}
		memset(dp, -1, sizeof(dp));
		printf("Case #%d: %d\n", iii, go(1,0));
	}
	return 0;
}
