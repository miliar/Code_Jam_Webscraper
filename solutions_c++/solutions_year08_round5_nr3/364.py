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

int n, m, N;
char g[128][128];
int dp[128][1024];
bool valid(int mask, int prev, int line)
{
	REP(i,m) if (g[line][i]=='x'&&(mask&(1<<i))) return false;
	REP(i,m) if ((mask&(1<<i))&&((i>0&&(prev&(1<<(i-1))))||(prev&(1<<(i+1))))) return false;
	REP(i,m) if ((mask&(1<<i)&&mask&(1<<(i+1)))) return false;
	return true;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int ntc;
	scanf("%d", &ntc);
	for (int itc=1; itc<=ntc; ++itc) {
		scanf("%d%d", &n, &m); N=1<<m;
		REP(i,n) scanf("%s", g[i]);
		REP(i,N) dp[0][i]=valid(i,0,0)?__builtin_popcount(i):0;
		for (int i=1; i<n; ++i) REP(j,N) {
			dp[i][j]=0;
			REP(k,N) if (valid(j,k,i)) dp[i][j]>?=dp[i-1][k]+__builtin_popcount(j);
		}
		int res=0;
		REP(i,N) res>?=dp[n-1][i];
		printf("Case #%d: %d\n", itc, res);
	}
}
