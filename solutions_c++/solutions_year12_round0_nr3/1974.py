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
int calc(int n, int b)
{
	int p = 1;
	while (p <= n) p *= 10;
	p /= 10;
	int m = n, res = 0;
	while (true)
	{
		int d = m % 10;
		m = m / 10 + p * d;
		if (d != 0 && b >= m && m > n) ++res;
		if (m == n) break;
	}
	return res;
}
int main()
{
	int t;
	scanf("%d", &t);
	for (int cs = 1; cs <= t; ++cs)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		int ans = 0;
		for (int n = a; n < b; ++n) ans += calc(n, b);
		printf("Case #%d: %d\n", cs, ans);
	}
	return 0;
}
