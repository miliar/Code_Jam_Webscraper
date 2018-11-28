#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
#include <queue>
#include <set>
#include <stack>
#include <list>

using namespace std;

//GyS Loves Algorithm
#define X first
#define Y second
#define all(x) x.begin(), x.end()
#define mk(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define rep(x, n) for (int x = 0; x < n; x++)
#define range(x, a, b)for (int x = a; x <= b; x++)
#define sz(x) x.size()
#define setv(x, y) memset(x, y, sizeof(x))
#define repi(it, x) for (typeof(x.begin()) it = x.begin(); it != x.end(); ++it)
#define pl() printf("\n")

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

pair<ll, int> r[1100];
ll px[1100], py[1100];

int main()
{
	int T;

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for (int cn = 1; cn <= T; cn++) {
		int n;

		ll w, l;
		scanf("%d%I64d%I64d", &n, &w, &l);
		for (int i = 0; i < n; i++) {
			scanf("%I64d", &r[i].X);
			r[i].Y = i;
		}
		sort(r, r + n);
		reverse(r, r + n);
		ll x = 0;
		for (int i = 0; i < n; i++) {
			int id1 = r[i].Y;
			if (x + r[i].X > w) {
				x = 0;
			}
			
			ll maxy = 0;
			while (true) {
				maxy = 0;
				for (int j = 0; j < i; j++) {
				int id = r[j].Y;
				if (px[id] - r[j].X < x + 2 * r[i].X
						&& px[id] + r[j].X > x) {
					maxy = max(maxy, py[id] + r[j].X);
				}
				}
				if (maxy <= l) {
					break;
				}
				x += r[i].X;
			}
			if (x == 0) {
				px[id1] = x;
				x += r[i].X;
			} else {
				px[id1] = x + r[i].X;
				x += 2 * r[i].X;
			}
			if (maxy == 0) { 
				py[id1] = maxy;
			} else {
				py[id1] = maxy + r[i].X;
			}
		}


		printf("Case #%d:", cn);
		for (int i = 0; i < n; i++) {
			printf(" %I64d %I64d", px[i], py[i]);
		}
		printf("\n");
	}
	return 0;
}
