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

const int maxn = 10009;

int t, n;
LL l, h;
LL ans;
LL freq[maxn];

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	FOR(tnum, 1, t)
	{
		scanf("%d%lld%lld", &n, &l, &h);
		REP(i, n)
			scanf("%lld", &freq[i]);
		sort(freq, freq + n);
		ans = 0;
		FOR(i, max(l, LL(0)), h)
		{
			bool bad = 0;
			REP(k, n)
			{
				if (freq[k] == 0) continue;
				if (freq[k] % i != 0 && i % freq[k] != 0)
				{
					bad = 1;
					break;
				}
			}
			if (!bad)  { ans = i; break; }
		}
		printf("Case #%d: ", tnum);
		if (ans == 0) printf("NO\n");
		else printf("%lld\n", ans);
	}
	return 0;
}
