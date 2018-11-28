#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <ctime>
#include <queue>

#define ll long long

using namespace std;

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

#define MAXN 1000000

ll L;
int n;
ll a[101];
ll f[300001];
void Solve(int id)
{
	cin >> L >> n;
	for (int i = 1; i <= n; i ++)
		cin >> a[i];
	sort(a + 1, a + 1 + n);
	ll limit = 200000;
	ll ans = 0;
	if (L > limit)
	{
		ans += (L - limit - 1) / a[n] + 1;
		L -= a[n] * ans;
	}
	memset(f, 0x3f, sizeof(f[0]) * (L + 1));
	ll max = f[0];
	f[0] = 0;
	ll v = 0;
	for (int i = 1; i <= L; i ++)
		for (int j = 1; j <= n; j ++)
			if (i >= a[j])
			{
				v = f[i - a[j]] + 1;
				if (v < f[i])
					f[i] = v;
			}
			else
				break;
	ans += f[L];
	cout << "Case #" << id << ": ";
	if (ans >= max)
		cout << "IMPOSSIBLE" << endl;
	else
		cout << ans << endl;
}


int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i ++)
		Solve(i);
	return 0;
}
