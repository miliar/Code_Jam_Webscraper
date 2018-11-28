#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <vector>
#include <time.h>

#define REP(i, n) for(int i=0, _n=(n); i<_n; i++)
#define REPD(i, n) for(int i=(n-1); i>=0; i--)
#define FOR(i, a, b) for(int i=a, _b=(b); i<=_b; i++)
#define FORD(i, a, b) for(int i=a, _b=(b); i>=_b; i--)
#define FILL(a, v) memset(&a, v, sizeof(a))
#define DB(x) cout << #x << " : " << x << endl
#define x first
#define y second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long LL;
typedef pair<int, int> pii;

const int maxn = 1000009;

int t, l, c, n, d[maxn], sum[maxn], a[maxn];
LL b, ans;

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	FOR(tnum, 1, t)
	{
		scanf("%d%lld%d%d", &l, &b, &n, &c);
		sum[0] = 0;
		ans = 0;
		REP(i, c)
		{
			scanf("%d", &d[i]);
		}
		REP(i, n)
		{
			a[i] = d[i%c];
		}
		REP(i, n)
		{
			if (ans + a[i]*2 < b)
			{
				ans += a[i]*2;
				a[i] = 0;
			}
			else
			{
				a[i] -= (b - ans) / 2;
				ans = b;
				break;
			}
		}
		sort(a, a+n, greater<int>());
		REP(i, n)
		{
			if (l) { ans += a[i]; l--; }
				else
					ans += 2*a[i];
		}
		printf("Case #%d: %lld\n", tnum, ans);
	}
	return 0;
}
