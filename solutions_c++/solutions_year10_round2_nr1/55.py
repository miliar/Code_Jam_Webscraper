#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <deque>
#include <map>
#include <stack>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))
#define sqr(x) ((x)*(x))
#define For(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,n) For(i,0,n)
#define re return
#define fi first
#define se second
#define y0 y47847892
#define y1 y47824262
#define fill(x, val) memset(x, val, sizeof(x))

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef long long ll;

#pragma comment(linker, "/STACK:16777216")

template<class T> T abs(T x) { return x > 0 ? x : -x;}

int n;
int m;

vector<vs> v;

vs add(string s) {
	replace(all(s), '/', ' ');
	vs ans;
	istringstream sin(s);
	string str;
	while (sin >> str)
		ans.pb(str);
	re ans;
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tt;
	cin >> tt;
	rep(tc, tt) {
		cout << "Case #" << tc + 1 << ": ";
		v.clear();
		cin >> n >> m;

		int ans = 0;
		rep(i, n) {
			string s;
			cin >> s;
			//cout << s << endl;
			vs u = add(s);
			v.pb(u);
		}

		rep(z, m) {
			string s;
			cin >> s;
			vs u = add(s);

			//cout << sz(u) << endl;

			int b = 0;
			int g = 0;
			rep(i, sz(v)) {
				//cout << sz(v[i]) << ' ' << sz(u) << endl;
				int f = 0;
				rep(j, min(sz(v[i]), sz(u)))
					if (v[i][j] != u[j]) {
						b = max(b, j);
						break;
					}
					else {
						if (j == sz(u) - 1)
							f = 1;
						b = max(b, j + 1);
					}

				if (f) {
					g = 1;
					break;
				}
			}

			//cout << z << ' ' << sz(u) << ' ' << b << endl;

			if (!g)
				ans += sz(u) - b;

			v.pb(u);
		}

		cout << ans << endl;
	}

	return 0;
}
