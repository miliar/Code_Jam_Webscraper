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
//#include <cmath>
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

int n, m, tc;
int x1, y1, x2, y2, x3, y3;
int a;
bool find()
{
	if (a>n*m) return false;
	x1=0; for (y1=0; y1<=n; ++y1)
	for (x2=0; x2<=m; ++x2) for (y2=0; y2<=n; ++y2)
	for (x3=0; x3<=m; ++x3) for (y3=0; y3<=n; ++y3) {
		int dx1=x2-x1, dy1=y2-y1;
		int dx2=x3-x1, dy2=y3-y1;
		if (abs(dx1*dy2-dx2*dy1)==a) return true;
	}
	return false;
//	for (dx1=0; dx1<=m; ++dx1) for (dx2=0; dx2<=m; ++dx2) for (dy2=0; dy2<=n; ++dy2) for (dy1=0;
	/*
	for (dx1=0; dx1<=m; ++dx1) for (dx2=0; dx2<=m; ++dx2) for (dy2=0; dy2<=n; ++dy2) {
		if (dx2!=0) dy1=(dx1*dy2-a)/dx2; else dy1=0;
		if (dy1>=dy2-n&&dy1<=dy2&&dx1*dy2-dx2*dy1==a) return true;
	}
	return false;
*/
}
int main()
{
	freopen("B-small-attempt4.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &tc);
	REP(itc, tc) {
		printf("Case #%d:", itc+1);
		scanf("%d%d%d", &n, &m, &a); swap(n,m);
		if (find()) {
			printf(" %d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
		} else printf(" IMPOSSIBLE\n");
	}
	return 0;
}

