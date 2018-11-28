#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <set>
#include <stack>
#include <string>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

#define FOR(i, k, n) for(int i = (k); i < (n); i++)
#define FORZ(i, n) FOR(i, 0, n)
#define pb push_back
#define sz(x) x.size()
#define all(x) x.begin(), x.end()
#define cl(x) memset(x, 0, sizeof(x))

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	vector <int> x;
	vector <int> y;
	long long N, n, a, b, c, d, x0, y0, m;
	scanf("%lld", &N);
	FORZ(i, N)
	{
		x.clear();
		y.clear();
		int ans = 0;
		scanf("%lld%lld%lld%lld%lld%lld%lld%lld", &n, &a, &b, &c, &d, &x0, &y0, &m);
		x.pb(x0);
		y.pb(y0);
		FORZ(j, n-1)
		{
			x0 = (a * x0 + b) % m;
			y0 = (c * y0 + d) % m;
			x.pb(int(x0));
			y.pb(int(y0));
		}
		FORZ(j, sz(x))
			FOR(k, j+1, sz(x))
				FOR(l, k + 1, sz(x))
					if((((x[j] + x[k] + x[l]) / 3) * 3 == x[j] + x[k] + x[l]) && (((y[j] + y[k] + y[l]) / 3) * 3 == y[j] + y[k] + y[l]))
						ans++;
		printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}