#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
using namespace std;

#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
#define PB push_back
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define MP make_pair
#define PRESENT(container, element) (container.find(element) != container.end())
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define INF 1000000000
#define EPS 1e-10
#define CLEAR(c,n) memset((c), (n), sizeof(c))

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
#define FI first
#define SE second
typedef long long LL;
typedef istringstream ISS;
typedef ostringstream OSS;

#define LEFT(x) ((x)*2+1)
#define RIGHT(x) ((x)*2+2)
#define UPPER(x) (((x)-1)/2)
int t, n, v, last;
int g[10000], c[10000];
int leaf[10000];
int dp[10000][2];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> t;
	REP(it,t) {
		scanf("%d%d", &n, &v);
		int last=(n-1)/2;
		REP(i,last) scanf("%d%d", g+i, c+i);
		REP(i,n-last) scanf("%d", leaf+i+last);

		for (int i=n-1; i>=last; --i) dp[i][leaf[i]]=0, dp[i][1-leaf[i]]=INF;
		for (int i=last-1; i>=0; --i) {
			if (g[i]==1) { // AND
				dp[i][1]=dp[LEFT(i)][1]+dp[RIGHT(i)][1];
				dp[i][0]=min(dp[LEFT(i)][0], dp[RIGHT(i)][0]);
			} else { // ALL
				dp[i][0]=dp[LEFT(i)][0]+dp[RIGHT(i)][0];
				dp[i][1]=min(dp[LEFT(i)][1], dp[RIGHT(i)][1]);
			}
			if (c[i]==1) {
				dp[i][1]<?=dp[LEFT(i)][1]+dp[RIGHT(i)][1]+1;
				dp[i][0]<?=min(dp[LEFT(i)][0], dp[RIGHT(i)][0])+1;
				dp[i][0]<?=dp[LEFT(i)][0]+dp[RIGHT(i)][0]+1;
				dp[i][1]<?=min(dp[LEFT(i)][1], dp[RIGHT(i)][1])+1;
			}
		}
		printf("Case #%d: ", it+1);
		if (dp[0][v]<=n) printf("%d\n", dp[0][v]);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}

