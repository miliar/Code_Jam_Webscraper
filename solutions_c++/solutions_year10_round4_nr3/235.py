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
bool g[128][128], bak[128][128];
bool check() {
	REP(i,128) REP(j,128) if (g[i][j]) return false;
	return true;
}
void go()
{
	MCPY(bak,g);
	REP(i,128) REP(j,128) if (i&&j) {
		if (bak[i][j]&&!bak[i-1][j]&&!bak[i][j-1]) g[i][j]=false;
		else if (bak[i-1][j]&&bak[i][j-1]) g[i][j]=true;
}
}
int main(int argc, char *argv[])
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int test_case;
	scanf("%d", &test_case);
	for (int test_case_id=1; test_case_id<=test_case; ++test_case_id) {
		int n, x1, y1, x2, y2;
		scanf("%d", &n); CLR(g,0);
		while (n--) {
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			FOR(x,x1,x2) FOR(y,y1,y2) g[x][y]=true;
		}
		int ans=0;
		while (!check()) {
			++ans;
			go();
		}
		fprintf(stderr, "Case %d of %d\n", test_case_id, test_case);
		printf("Case #%d: %d\n", test_case_id, ans);
	}
}

