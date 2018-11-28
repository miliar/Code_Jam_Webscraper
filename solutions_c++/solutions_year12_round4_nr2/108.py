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
typedef vector<long long> VL;
int w, l, n;
VPII r;
VL x, y;
long long sqr(long long x)
{
	return x * x;
}
void init()
{
	scanf("%d%d%d", &n, &w, &l);
	r.resize(n);
	rep(i, n)
	{
		scanf("%d", &r[i].first);
		r[i].second = i;
	}
}
bool gao()
{
	rep(i, n)
	{
		long long tx = (long long)rand() * rand() % (w + 1);
		long long ty = 0;
		rep(j, i)
		{
			long long a = abs(tx - x[j]);
			long long b = r[i].first + r[j].first;
			if (a >= b) continue;
			long long z = y[j] + sqrt(b * b - a * a - 1) + 1;
			ty = max(ty, z);
		}
		if (ty > l) return false;
		x[i] = tx;
		y[i] = ty;
	}
	return true;
}
void solve()
{
	x.resize(n);
	y.resize(n);
	sort(r.rbegin(), r.rend());
	while(!gao());
}
//bool check()
//{
//	rep(i, n)
//	{
//		if (x[i] < 0 || x[i] > w || y[i] < 0 || y[i] > l) return false;
//		rep(j, i)
//		{
//			long long d = sqr(x[i] - x[j]) + sqr(y[i] - y[j]);
//			if (d < sqr(
//		}
//	}
//}
int main()
{
	int t;
	scanf("%d", &t);
	for (int cs = 1; cs <= t; ++cs)
	{
		init();
		printf("Case #%d:", cs);
		solve();
		VI tx(n), ty(n);
		rep(i, n)
		{
			tx[r[i].second] = x[i];
			ty[r[i].second] = y[i];
		}
		rep(i, n) printf(" %d %d", tx[i], ty[i]);
		puts("");
	}
	return 0;
}
