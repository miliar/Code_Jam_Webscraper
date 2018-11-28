#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
using namespace std;
#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
#define CLR(c,n) memset(c,n,sizeof(c))
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define CONTAIN(container, it) (container.find(it)!=container.end())
#define MCPY(dest,src) memcpy(dest,src,sizeof(src))
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;
const double EPS=1e-9;
const double PI=acos(-1);
const int INF=0x3F3F3F3F;
int n, N;
int cnt[11],miss[1<<10], price[11][1<<10];
int dp[11][1<<10][11];
int main(int argc, char *argv[])
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int test_case;
	scanf("%d", &test_case);
	for (int test_case_id=1; test_case_id<=test_case; ++test_case_id) {
		CLR(dp,0);
		scanf("%d", &n); N=1<<n; cnt[0]=N;
		REP(i,N) scanf("%d", miss+i);
		FOR(i,1,n) {
			cnt[i]=cnt[i-1]/2;
			REP(j,cnt[i]) scanf("%d", price[i]+j);
		}
		assert(cnt[n]==1);
		CLR(dp,INF);
		REP(i,N) FOR(j,0,miss[i]) dp[0][i][j]=0;
		FOR(i,1,n) REP(j,cnt[i]) {
			int j1=j*2, j2=j1+1;
			FOR(k,0,n) dp[i][j][k]<?=dp[i-1][j1][k]+dp[i-1][j2][k]+price[i][j]<?dp[i-1][j1][k+1]+dp[i-1][j2][k+1];
/*			int a1=minmiss[i-1][j1]-minmiss[i][j], a2=minmiss[i-1][j2]-minmiss[i][j];
			dp[i][j][0]=dp[i-1][j1][a1]+dp[i-1][j2][a2]+price[i][j];
			FOR(k,1,minmiss[i][j]) {
//				if (minmiss[i-1][j1]==minmiss[i-1][j2])
					dp[i][j][k]=min(dp[i-1][j1][k+a1]+dp[i-1][j2][k+a2]+price[i][j], dp[i-1][j1][k-1+a1]+dp[i-1][j2][k-1+a2]);
//				else if (minmiss[i-1][j1]<minmiss[i-1][j2])
//					dp[i][j][k]=min(dp[i-1][j1][k]+dp[i-1][j2]*/
//			}
			//FOR(k,0,minmiss[i][j]) cerr << i << " " << j << " " << k << " " << dp[i][j][k] << endl;
		}
		fprintf(stderr, "Case %d of %d\n", test_case_id, test_case);
		printf("Case #%d: %d\n", test_case_id, dp[n][0][0]);
	}
}

