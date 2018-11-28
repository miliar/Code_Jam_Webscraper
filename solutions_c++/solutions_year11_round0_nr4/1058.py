#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define forv(i, v) forn(i, (v).size())
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define contains(c, v) binary_search(all(c), v)

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef long double ld;
const int NMAX = 1005;
double E[NMAX][NMAX];

void solve(int N)
{
	typedef vector<double> vd;
	vector<vd> t(N + 1, vd(N + 1)), p(N + 1, vd(N + 1));
	for1(n, N) {
		p[n][1] = 1.0 / n;
		p[n][n] = 1.0;
		for1(i, n) p[n][n] /= i;
		for(int k = 2; k < n; ++k) {
			p[n][k] = 0;
			for(int i = 0; i <= n - k; ++i) {
				p[n][k] += p[n - i - 1][k - 1];
			}
			p[n][k] /= n;
		}
		{
			double cur = 1.0;
			double sum = 1.0;
			for(int i = n; i > 0; --i) {
				cur /= i;
				sum += cur;
			}
			t[n][n] = 1.0 / sum;
		}
		for(int i = n - 1; i >= 0; --i) {
			t[n][i] = t[n][i + 1] / (i + 1);
		}
		E[n][n] = 0.0;
		for(int k = 2; k < n; ++k) {
			E[n][k] = 0.0;
			forn(i, n - k + 1) {
				E[n][k] += t[n - k][i] * (E[i + 1][1] + E[n - i - 1][k - 1]);
			}
		}
		E[n][1] = p[n][1];
		for(int i = 2; i <= n; ++i) {
			E[n][1] += p[n][i] * (E[n][i] + 1.0);
		}
		E[n][1] /= 1.0 - p[n][1];
		if (n == 1) {
			E[n][1] = 0.0;
		}
	}
}

vi cycles(vi v)
{
	vi used(v.size());
	vi result;
	forv(i, v) {
		if (used[i]) continue;
		int cnt = 0;
		int u = i;
		while (!used[u]) {
			used[u] = true;
			u = v[u];
			++cnt;
		}
		result.pb(cnt);
	}
	return result;
}

double d[1004];

void stupid(int N)
{
	d[1] = 0.0;
	for(int n = 2; n <= N; ++n) {
		vi p(n);
		forn(i, n) p[i] = i;
		do {
			vi c = cycles(p);
			if (c.size() == 1) continue;
			double sum = 0.0;
			forv(i, c) sum += d[c[i]];
			d[n] += sum;
		} while (next_permutation(all(p)));
		for1(i, n) d[n] /= i;
		d[n] = n * (d[n] + 1) / (n - 1);
	}
}

int main()
{
	//freopen("input.txt", "rt", stdin);
	ios_base::sync_with_stdio(false);
	int tn; cin >> tn;
	//solve(104);
	//stupid(10);
	cout.precision(10);
	cout << fixed;
	forn(it, tn) {
		int n; cin >> n;
		vi v(n);
		forn(i, n) cin >> v[i], v[i]--;
		double ans = n;
		forn(i, n) if (v[i] == i) ans -= 1.0;
		cout << "Case #" << it+1 << ": " << ans << endl;
	}

	return 0;
}
