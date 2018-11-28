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
typedef long long LL;
typedef long double LD;
const int max_h = 1000000000;
const long double eps = 1e-12;
int n;
VI p, h;
void init()
{
	scanf("%d", &n);
	p.resize(n - 1);
	rep(i, n - 1)
	{
		scanf("%d", &p[i]);
		--p[i];
	}
}
bool solve()
{
	h.resize(n);
	fill(h.begin(), h.end(), 0);
	int tries = 100000;
	while (tries-- > 0)
	{
		bool done = true;
		rep(i, n - 1)
		{
			int j = p[i];
			LL th = h[j];
			for (int k = i + 1; k < j; ++k)
			{
				LL y = (LL) floor(((LD) (j - i) * h[k] - (LD) (j - k) * h[i] + k - i) / (k - i)) + eps;
				th = max(th, y);
			}
			for (int k = j + 1; k < n; ++k)
			{
				LL y = (LL) floor(((LD) (j - i) * h[k] - (LD) (j - k) * h[i] + k - i - 1) / (k - i)) + eps;
				th = max(th, y);
			}
			if (th > max_h) return false;
			if (h[j] != th)
			{
				h[j] = th;
				done = false;
			}
		}
		if (done) return true;
	}
	return false;
}
int main()
{
	int t;
	scanf("%d", &t);
	for (int cs = 1; cs <= t; ++cs)
	{
		printf("Case #%d:", cs);
		init();
		if (solve())
		{
			rep(i, n) printf(" %d", h[i]);
			puts("");
		}
		else
		{
			puts(" Impossible");
		}
	}
	return 0;
}
