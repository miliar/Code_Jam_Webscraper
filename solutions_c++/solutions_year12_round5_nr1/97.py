#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <numeric>
#include <functional>
#define rep(i,n) for(int i=0;i<(n);++i)
#define foreach(i,v) for(__typeof(v.begin()) i=v.begin();i!=v.end();++i)
#define ass(v) (v)||++*(int*)0;
using namespace std;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef vector<double> VD;
struct info
{
	int l, p, i;
	bool operator < (const info &o) const
	{
		int a = l * o.p;
		int b = p * o.l;
		if (a < b) return true;
		if (a > b) return false;
		return i < o.i;
	}
};
void solve()
{
	int n;
	scanf("%d", &n);
	vector<info> all(n);
	rep(i, n) scanf("%d", &all[i].l);
	rep(i, n) scanf("%d", &all[i].p);
	rep(i, n) all[i].i = i;
	sort(all.begin(), all.end());
	rep(i, n) printf(" %d", all[i].i);
	puts("");
}
int main()
{
	int t;
	scanf("%d", &t);
	for (int cs = 1; cs <= t; ++cs)
	{
		printf("Case #%d:", cs);
		solve();
	}
	return 0;
}
