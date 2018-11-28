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
int n, z;
VI d, l;
void init()
{
	scanf("%d", &n);
	d.resize(n);
	l.resize(n);
	rep(i, n) scanf("%d%d", &d[i], &l[i]);
	scanf("%d", &z);
}
bool solve()
{
	VI f(n);
	f[0] = d[0] * 2;
	rep(i, n)
	{
		if (f[i] >= z) return true;
		for (int j = i + 1; j < n; ++j)
		{
			if (f[i] < d[j]) break;
			int q = max(d[i], d[j] - l[j]);
			f[j] = max(f[j], d[j] * 2 - q);
		}
	}
	return false;
}
int main()
{
	int t;
	scanf("%d", &t);
	for (int cs = 1; cs <= t; ++cs)
	{
		init();
		printf("Case #%d: %s\n", cs, solve() ? "YES" : "NO");
	}
	return 0;
}
