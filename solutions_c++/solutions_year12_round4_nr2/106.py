#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <vector>
#include <fstream>
#include <sstream>
#include <queue>
#include <cmath>
#include <set>
using namespace std;
#define L(s) (int)((s).size())
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
#define inf 1000000000
#define all(s) (s).begin(), (s).end()
#define ll long long
#define VI vector<int>
#define ull unsigned ll
int w, l, n, t;
pii a[1111], ans[1111];
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int curt = 1; curt <= t; ++curt) {
		cerr << curt << endl;
		cin >> n >> w >> l;
		for(int i = 0; i < n; ++i) {
			cin >> a[i].x; a[i].y = i;
		}
		sort(a, a + n);
		reverse(a, a + n);
		int sx = -a[0].x;
		int on = n;
		while(n > 0) {
			sort(a, a + n);
			reverse(a, a + n);
			int sy = -a[0].x;
			int nx = -inf;
			for(int i = 0; i < n; ++i) {
				if (sy + a[i].x <= l) {
					ans[a[i].y] = mp(max(sx + a[i].x, 0), sy + a[i].x);
					sy += 2 * a[i].x;
					if (nx == -inf) nx = sx + 2 * a[i].x;
					a[i].y = -1;
				}
			}
			for(int i = 0; i < n; ++i)
				if (a[i].y == -1) {
					swap(a[i], a[n - 1]);
					--n; --i;
				}
			sx = nx;
		}
		printf("Case #%d:", curt);
		for(int i = 0; i < on; ++i) {
			printf(" %d %d", ans[i].x, ans[i].y);
			if (ans[i].x > w) {
				cerr << "ERROR\n";
				exit(0);
			}
		}
		printf("\n");
	}
}
