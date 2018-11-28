#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
#define PB push_back
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define MP make_pair
#define PRESENT(container, element) (container.find(element) != container.end())
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define CLEAR(c,n) memset(c,n,sizeof(c))
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double PI=acos(-1.0);
const double EPS=1e-11;
const int INF=1000000000;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large","w",stdout);
	int n, t;
	LL a, b, c, d, x, y, m;
	cin >> t;
	REP(ic,t) {
		cin>>n>>a>>b>>c>>d>>x>>y>>m;
		LL cnt[3][3], tot=0; CLEAR(cnt,0);
		REP(i,n) {
			++cnt[x%3][y%3];
			x=(a*x+b)%m; y=(c*y+d)%m;
		}
		REP(x1,3) REP(y1,3) REP(x2,3) REP(y2,3) {
			int x3=(6-x1-x2)%3, y3=(6-y1-y2)%3;
			if (x1!=x2||y1!=y2) tot+=cnt[x1][y1]*cnt[x2][y2]*cnt[x3][y3];
		}
		REP(x1,3) REP(y1,3) tot+=cnt[x1][y1]*(cnt[x1][y1]-1)*(cnt[x1][y1]-2);
		printf("Case #%d: %I64d\n", ic+1, tot/6);
	}
	return 0;
}
