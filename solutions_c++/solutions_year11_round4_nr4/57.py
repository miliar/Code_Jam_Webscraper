#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <queue>
#include <bitset>
#include <cmath>
#include <sstream>
#include <string>
#include <vector>
#include <ppl.h>

#define mp make_pair
#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;
using namespace Concurrency;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T x) {return x > 0 ? x : (-x); }
template<class T> T sqr(T x) {return x * x; }

critical_section criticalSection;

const int inf = 1000 * 1000 * 1000;

const int maxn = 570;

struct Problem {
	int problemId;
	// problem data
	vi g[maxn];
	int n, m;

	int r1, r2;
	
	vi d[maxn];

	// some data

	void read() {
		cin >> n >> m;
		for (int i = 0; i < m; ++i) {
			string s;
			cin >> s;
			for (int j = 0; j < sz(s); ++j)
				if (s[j] == ',') s[j] = ' ';
			int x, y;
			sscanf(s.c_str(), "%d%d", &x, &y);
			g[x].pb(y);
			g[y].pb(x);
		}
	}

	vi add(vi v, int x) {
		++v[0];
		for (int i = 0; i < sz(g[x]); ++i) {
			if (v[g[x][i] + 1] == 0)
				v[g[x][i] + 1] = -1;
		}
		v[x + 1] = 1;
		return v;
	}

	bool cmp(const vi& p, const vi& q) {
		if (p[0] != q[0]) return p[0] < q[0];
		int64 sp = 0, sq = 0;
		for (int i = 1; i < sz(p); ++i)
			if (p[i] < 0) sp += p[i];
		for (int i = 1; i < sz(q); ++i)
			if (q[i] < 0) sq += q[i];
		return sp < sq;
	}

	void solve() {
		criticalSection.lock();
		cerr << "Solving case " << problemId << "\n";
		criticalSection.unlock();
		vi vinf(n + 1, 0);
		vinf[0] = inf;
		vi u(n, 0);
		for (int i = 0; i < n; ++i)
			d[i] = vinf;
		d[0] = add(vi(n + 1, 0), 0);
		vi res = vinf;
		while (1) {
			vi val = vinf;
			int ind = -1;
			for (int i = 0; i < n; ++i)
				if (!u[i] && cmp(d[i], val))
					val = d[i], ind = i;
			if (ind == -1) break;
			u[ind] = true;
			if (d[ind][2] != 0) {
				if (cmp(d[ind], res))
					res = d[ind];
				continue;
			}
			for (int i = 0; i < sz(g[ind]); ++i) {
				int y = g[ind][i];
				vi tmp = add(d[ind], y);
				if (cmp(tmp, d[y]))
					d[y] = tmp;
			}
		}
		r1 = res[0] - 1;
		r2 = 0;
		for (int i = 1; i <= n; ++i)
			if (res[i] < 0)
				r2 -= res[i];
	}

	void save() {
		cout << r1 << " " << r2 << "\n";
	}
};

int main()
{
	//freopen("", "r", stdin);
	//freopen("", "w", stdout);
	int nc;
	cin >> nc;
	vector<Problem> problems(nc);
	for (int it = 0; it < nc; ++it) {
		problems[it].problemId = it;
		problems[it].read();
	}

	for_each(all(problems), 
		[&](Problem& p) {
			p.solve();
		}
	);	

	for (int it = 0; it < nc; ++it) {
		printf("Case #%d: ", it + 1);
		problems[it].save();
	}
	return 0;
}
