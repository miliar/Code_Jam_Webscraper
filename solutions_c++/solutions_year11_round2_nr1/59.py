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
		int n;
		cin >> n;
		double wp[1000], owp[1000], oowp[1000];
		memset(wp, 0, sizeof(wp));
		memset(owp, 0, sizeof(owp));
		memset(oowp, 0, sizeof(oowp));
		vi op[1000];
		string s[1000];
		for (int i = 0; i < n; i++) cin >> s[i];
		for (int i = 0; i < n; i++) {
			int k = 0, w = 0;
			for (int j = 0; j < n; j++) if (s[i][j] != '.') {
				k++;
				if (s[i][j] == '1') w++;
				op[i].pb(j);
			}
			wp[i] = (double) w / (double) k;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < (int)op[i].size(); j++) {
				int u = op[i][j];
				int m, w; m = w = 0;
				for (int k = 0; k < n; k++) if (k != i && s[u][k] != '.') {
					m++; if (s[u][k] == '1') w++;
				}
				owp[i] += (double) w / (double) m;
			}
			owp[i] /= (double)op[i].size();
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < (int)op[i].size(); j++) oowp[i] += owp[op[i][j]];
			oowp[i] /= (double)op[i].size();
		}
		cout << "Case #" << I + 1 << ":" << endl;
		for (int i = 0; i < n; i++) printf("%.10lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
	}
	return 0;
}
