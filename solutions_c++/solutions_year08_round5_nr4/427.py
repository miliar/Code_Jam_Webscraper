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
#define REP(i,n) for (int i=1; i<=(n); ++i)
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
int h, w, r;
#define MOD 10007
int dp[128][128];
bool valid[128][128];
int main()
{
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D-small-attempt1.out","w",stdout);
	int ntc;
	scanf("%d", &ntc);
	for (int itc=1; itc<=ntc; ++itc) {
		scanf("%d%d%d", &h, &w, &r);
		CLEAR(dp,0); CLEAR(valid,true);
		int x, y;
		REP(i,r) scanf("%d%d", &x, &y), valid[x][y]=false;
		if (valid[1][1]) dp[1][1]=1;
		REP(i,h) REP(j,w) if (valid[i][j]) {
			if (i>2&&j>1) dp[i][j]+=dp[i-2][j-1];
			if (i>1&&j>2) dp[i][j]+=dp[i-1][j-2];
			dp[i][j]%=MOD;
		}
		printf("Case #%d: %d\n", itc, dp[h][w]);
	}
}
