#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <sstream>
#include <bitset>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
typedef unsigned long long UL;
typedef long double LD;
typedef pair<int,int> PII;

const int INF = 1000*1000*1000+1;
#define FOR(x,b,e) for (int x = (b); x < (e); ++x)
#define FORD(x,b,e) for (int x = (b); x >= (e); --x)
#define REP(x,n) for (int x = 0; x < (n); ++x)
#define VAR(v,n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i,c) for (VAR(i,(c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

VVI dp;
int n, m;
VI matc, lim;
void scase() {
	int p;
	scanf("%d",&p);
	n=1<<p, m = n-1;
	matc = VI(m);
	lim = VI(n);
	REP(i,n) { scanf("%d",&lim[i]); lim[i] = p-lim[i]; }
	dp = VVI(m, VI(p,INF));
	REP(i,m) scanf("%d",&matc[i]);
	VI maxl(m);
	REP(i,n/2) REP(j,p) {
		maxl[i] = max(lim[2*i],lim[2*i+1]);
		if (maxl[i] - j <= 0) dp[i][j]=0;
		if (maxl[i] - j - 1 <= 0) 
			dp[i][j]=min(dp[i][j],matc[i]);
	}
	int back=n/2;
	int z=1;
	int cnt=0, curpw=n/4;
	FOR(i,n/2,m) {
		back = curpw*2 - cnt;
		maxl[i] = max(maxl[i-back],maxl[i-back+1]);
//		cout << i << ' ' << i-back << ' ' << i-back + 1 << ' ' << maxl[i-back] << ' ' << maxl[i-back+1] << endl;
		REP(j,p-z) {
		//	cout << i << ' '  << j << ' ' << dp[i-back][j+1] << ' ' << dp[i-back+1][j+1] << endl;
			dp[i][j] = matc[i] + dp[i-back][j+1] + dp[i-back+1][j+1];
			dp[i][j] = min(dp[i][j], dp[i-back][j] + dp[i-back+1][j]);
			if (dp[i][j] > INF) dp[i][j] = INF;
		}
		++cnt;
		if (cnt == curpw) { cnt=0; curpw /= 2; ++z; }
	}
//	REP(i,m) cout << maxl[i] << ' '; cout << endl;
//	REP(i,m) REP(j,p) printf("dp[%d][%d]=%d\n",i, j, dp[i][j]);
	printf("%d\n",dp[m-1][0]);

}

int main() {
	int z;
	scanf("%d",&z);
	REP(i,z) {
		printf("Case #%d: ",i+1);
		scase();
	}

	return 0;
}
