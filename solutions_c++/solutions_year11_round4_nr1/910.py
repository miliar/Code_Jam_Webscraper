
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>

#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

#define forn(i, n) for (i = 0; i < (int)(n); ++i)
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;

const int maxn = 1000 + 5;

double b[maxn], e[maxn], w[maxn];

struct my{
	double len, v, vv;
	my () {}
	my (double _len, double _v, double _vv): len(_len), v(_v), vv(_vv) {}
};

bool myLess(const my &a, const my&b)
{
	return a.v > b.v;
}

vector <my> a;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);


	int T, i, j;
	cin >> T;
	int it;
	double ans;
	double x, s, r, t;
	int n;
	forn(it, T) {
		ans = 0;
		cin >> x >> s >> r >> t >> n;
		double se = 0; 
		a.clear();
		forn(i, n) {
			cin >> b[i] >> e[i] >> w[i];
			if (i == 0)
				se += b[i];
			if (i == n - 1)
				se += x - e[i];
			if (i > 0)
				se += b[i] - e[i - 1];
			a.pb(my(e[i] - b[i], s + w[i], w[i]));
		}
		a.pb(my(se, s, 0));
		sort(a.rbegin(), a.rend(), myLess);

		int sz = a.size();
		forn(i, sz) {
			if (t*(a[i].vv + r) <= a[i].len) {
				ans += t;
				a[i].len -= t*(a[i].vv + r);
				ans += a[i].len / (s + a[i].vv);
				t = 0;
			} else {
				double delta = a[i].len / (a[i].vv + r);
				t -= delta;
				ans += delta;
			}
		}

		printf("Case #%d: %.9f\n", it + 1, ans); 
	}

	return 0;
}
