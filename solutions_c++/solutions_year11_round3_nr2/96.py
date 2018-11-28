#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <ctype.h>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define For(i, n) for (int i = 0; i < n; i ++)
#define foreach(x, i) for (__typeof(x.begin()) i; i != x.end(); i ++)
typedef long long int ll;

using namespace std;

int L, n, C;
ll T;
const int N = 1000000;
int a[N];
ll s[N];
void update(int &a, int b)
{
	if (b < a)
		a = b;
}

int cnt[1000];
bool cmp(int x, int y)
{
	return a[x] < a[y];
}

int id[1000];
ll calc(int remain)
{
	ll ret = 0;
	for (int i = 0; i < C; i ++)
		id[i] = i;
	sort(id, id + C, cmp);
	for (int i = C - 1; i >= 0 && remain; i --)
	{
		ll t = min(cnt[id[i]], remain);
		ret += t * a[id[i]];
		remain -= t;
	}
	return ret;
}

void solve()
{
	scanf("%d%lld%d%d", &L, &T, &n, &C);
	ll sum = 0, ans = 0;
	for (int i = 0; i < C; i ++)
		scanf("%d", &a[i]), s[i] = (sum += a[i]);
	ans = n / C * sum * 2 + ((n % C) ? s[n % C - 1] * 2 : 0);
	if (T < ans)
	{
		for (int i = 0; i < C; i ++)
			cnt[i] = n / C + (i < n % C);
		int p = T / (sum * 2);
		ll ts = sum * p * 2;
		for (int i = 0; i < C; i ++)
			cnt[i] -= T / (sum * 2);
		int t = 0;
		while (ts < T)
		{
			cnt[t] --;
			ts += a[t ++] * 2, p ++;
		};
		ans -= max((ts - T) / 2 + calc(L - 1), calc(L));
	}
	printf("%lld\n", ans);
}


int main()
{
	int t; scanf("%d", &t);
	For (i, t) printf("Case #%d: ", i + 1), solve();
	return 0;
}

