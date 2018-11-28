#pragma comment(linker, "/STACK:512000000")

#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define forv(i, v) forn(i, (v).size())
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef long double ld;

typedef vector<int> VI;
typedef vector<bool> VB;
typedef pair<int, int> Edge;
typedef vector<vector<Edge> > Graph;

void init()
{
	freopen("input.txt", "rt", stdin);
}
vector<VI> w;
int r, c, d;

bool good(int x, int y, int k) {
	ld cx = x + k / 2.0;
	ld cy = y + k / 2.0;
	ld sx = 0, sy = 0;
	for(int i = x; i < x + k; ++i) {
		for(int j = y; j < y + k; ++j) {
			if (i == x && j == y) continue;
			if (i == x && j == y + k - 1) continue;
			if (i == x + k - 1 && j == y) continue;
			if (i == x + k - 1 && j == y + k - 1) continue;
			ld xx = i + 0.5;
			ld yy = j + 0.5;
			sx += (xx - cx) * (d + w[i][j]);
			sy += (yy - cy) * (d + w[i][j]);
		}
	}
	const static ld EPS = 1e-8;
	return fabsl(sx) < EPS && fabsl(sy) < EPS;
}

int main()
{
	//init();

	int tc; cin >> tc;
	forn(it, tc) {
		cin >> r >> c >> d;
		w = vector<VI>(r);
		forn(i, r) {
			string s; cin >> s;
			forv(j, s) w[i].pb(s[j]-'0');
		}
		int ans = -1;
		for(int k = 3; k <= min(r, c); ++k) {
			for(int i = 0; i + k <= r; ++i) {
				for(int j = 0; j + k <= c; ++j) {
					if (good(i, j, k))
						ans = max(ans, k);
				}
			}
		}
		cout << "Case #" << it + 1 << ": ";
		if (ans == -1) cout << "IMPOSSIBLE";
		else cout << ans;
		cout << endl;
	}

	return 0;
}
