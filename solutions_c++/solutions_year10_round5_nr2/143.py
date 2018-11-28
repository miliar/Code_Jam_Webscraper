#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <sstream>
#include <string>

using namespace std;

typedef long long ll;
typedef stringstream sstream;

#define fn(i,n)	for (int i = 0; i < n; ++i)

#define filename "B-small-attempt0"

int gcd (int a, int b) {
	return b ? gcd (b, a % b) : a;
}

int b[1024];
int m[10240];

int main()
{
	freopen (filename ".in", "rt", stdin);
	freopen (filename ".out", "wt", stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		ll l;
		int n;
		int maxb;
		cin >> l >> n;
		for (int i = 0; i < n; ++i)
			cin >> b[i];
		int g = b[0];
		maxb = b[0];
		for (int i = 1; i < n; ++i) {
			if (b[i] > maxb) maxb = b[i];
			g = gcd (g, b[i]);
		}

		cout << "Case #" << test << ": ";
		if (l % g != 0) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		memset (m, 0x3f, sizeof(m));
		m[0] = 0;
		int border = 10240;
		int inf = 0x3f3f3f3f;
		for (int i = 0; i < border; ++i) {
			if (m[i] == inf)
				continue;
			for (int j = 0; j < n; ++j)
				if (i + b[j] < border && m[i + b[j]] > m[i] + 1)
					m[i + b[j]] = m[i] + 1;
		}
		ll ans = 0x3f3f3f3f3f3f3f3fLL;
		ll ret = l % maxb;
		ll d = l / maxb;
		for (ll i = 0; (ret + i * maxb) < border; ++i) {
			int ind = ret + i * maxb;
			if (m[ind] != inf &&
				m[ind] + d - i < ans)
				ans = m[ind] + d - i;
		}
		cout << ans << endl;
	}

	return 0;
}