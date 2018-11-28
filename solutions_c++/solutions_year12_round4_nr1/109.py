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
int t, n, d;
bool f[11111][11111];
pii a[11111];
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int curt = 1; curt <= t; ++curt) {
		cerr << curt << endl;
		cin >> n;
		for(int i = 1; i <= n; ++i) cin >> a[i].x >> a[i].y;
		cin >> d;
		a[0].x = 0; a[0].y = a[1].x;
		a[n + 1].x = d; a[n + 1].y = 0;
		n += 2;
		memset(f, 0, sizeof(f));
		f[1][0] = 1;
		for(int i = 1; i < n - 1; ++i) {
			int lim = n - 1;
			for(int j = 0; j < i; ++j) {
	//			cerr << i << " " << j << " " << f[i][j] << endl;
				int canfly = min(a[i].x - a[j].x, a[i].y);
	//			cerr << a[1].x - a[0].x << " " << a[1].y << endl;
	//			cerr << canfly << endl;
				while(a[lim].x - a[i].x > canfly) {
					--lim;
				}
	//			cerr << lim << endl;
				if (f[i][j]) f[lim][i] = 1;
			}
			for(int j = n - 1; j > i; --j) {
				if (f[j][i]) f[j - 1][i] = 1;
			}
		}
		bool ok = 0;
		for(int j = 0; j < n; ++j) ok |= f[n - 1][j];
		printf("Case #%d: ", curt);
		if (ok) printf("YES\n"); else printf("NO\n");
	}
}
