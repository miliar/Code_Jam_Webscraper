#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define sqr(x) ((x)*(x))
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define re return

#ifdef ONLINE_JUDGE
#pragma comment(linker, "/STACK:16777216")
#endif

using namespace std;

typedef vector <int> vi;
typedef vector <vi> vvi;
typedef long long ll;
typedef long double ld;
typedef pair <int, int> ii;
typedef vector <ii> vii;

template <class T> T abs(const T & a) {
	return a > 0 ? a : -a;
}

template <class T> int sgn(const T & a) {
	return a > 0 ? 1 : (a < 0 ? -1 : 0);
}

#ifdef ONLINE_JUDGE
const double M_PI = 2.0 * acos(1.0);
#endif

int main()
{
	int T;
	cin >> T;
	for (int I = 0; I < T; I++) {
		cout << "Case #" << I + 1 << ": ";
		int n;
		cin >> n;
		vector <int> a[2];
		int p[100];
		for (int i = 0; i < n; i++) {
			string s; int x;
			cin >> s >> x;
			if (s == "O") {
				p[i] = 0;
				a[0].pb(x);
			} else {
				p[i] = 1;
				a[1].pb(x);
			}
		}
		/*for (int i = 0; i < 2; i++) {
			for (int j = 0; j < (int)a[i].size(); j++) cerr << a[i][j]<< ' '; cerr << endl;
		}
		for (int i = 0; i < n; i++) cerr << p[i]; cerr << endl;*/
		int x[2], cur[2];
		x[0] = x[1] = 1; cur[0] = cur[1] = 0;
		int ans = 0;
		for (int i = 0; i < n; i++) {
			//cerr << ans << ' ' << x[0] << ' ' << x[1] << ' ' << cur[0] << ' ' << cur[1] << endl;
			while (x[p[i]] != a[p[i]][cur[p[i]]]) {
				ans++;
				x[p[i]] += sgn(a[p[i]][cur[p[i]]] - x[p[i]]);
				if (cur[1 - p[i]] != (int) a[1 - p[i]].size()) x[1 - p[i]] += sgn(a[1 - p[i]][cur[1 - p[i]]] - x[1 - p[i]]);
			}
			ans++;
			if (cur[1 - p[i]] != (int) a[1 - p[i]].size()) x[1 - p[i]] += sgn(a[1 - p[i]][cur[1 - p[i]]] - x[1 - p[i]]);
			cur[p[i]]++;
		}
		//re 0;
		cout << ans << endl;
	}
	return 0;
}
