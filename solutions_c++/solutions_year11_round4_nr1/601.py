#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <utility>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int) (n); ++i)
#define fore(i, a, b) for(int i = (int) (a); i < (int) (b); ++i)

#define ll long long
#define ld long double
#define PLL pair <ld, ld>
#define PII pair <int, int>
#define pb push_back

const ld EPS = 1e-9;
const int MAXN = 3000;
const int INF = (int)(1e9 + 1e-9);

int n;
int d[MAXN], w[MAXN];

vector <PII> v;

int main()
{
    freopen("input.txt","rt", stdin);
    freopen("a.out", "wt", stdout);    
	
	int tk;
	cin >> tk;

	cout.precision(9);
	cout.setf(ios::fixed);

	forn(ii, tk){
		int x, s, r, t, n;
		cin >> x >> s >> r >> t >> n;
		r = max(r, s);
		int q = x;

		r -= s;
		v.clear();
		v.reserve(n + 1);

		forn(i, n){
			int l1, r1, w, d;
			cin >> l1 >> r1 >> w;
			w += s;
			d = r1 - l1;
			q -= d;

			v.pb(PII(w, d));
		}

		if (q){
			v.pb(PII(s, q));
		}

		n = v.size();

		sort(v.begin(), v.end());

		ld ans = 0;
		ld T = t;
		forn(i, n){
			ld p = min(T, (ld)(v[i].second / (.0 + v[i].first + r)));

			T -= p;
			ans += p + (v[i].second - (v[i].first + r) * p) / v[i].first;
		}
		
		printf("Case #%d: %.9Lf\n", ii + 1, ans);
	}

	return 0;
}

