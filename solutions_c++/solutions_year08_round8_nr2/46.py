#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:30000000")

#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <sstream>
#include <cassert>
#include <utility>

using namespace std;

#define EPS 1E-8
const int INF = (int)1E+9;

#define C_IN_FILE "input.txt"
#define C_OUT_FILE "output.txt"

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forv(i, v) for (int i = 0; i < (int)(v.size()); ++i)
#define fors(i, s) for (int i = 0; i < (int)(s.length()); ++i)
#define all(a) a.begin(), a.end()
#define pb push_back
#define PII pair<int, int>
#define mp make_pair
#define VI vector<int>
#define VS vector<string>
#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())
typedef long long int64;

struct seg {
	int l, r, c;
};

bool operator < (const seg& f, const seg& s) {
	return mp(f.l, f.r) < mp(s.l, s.r);
}

int n, kl, nc, ans;
vector<seg> segs;
vector<string> cols;

void outdata() {
	if (ans >= INF) {
		cout << "IMPOSSIBLE" << endl;
	} else {
		cout << ans << endl;
	}
}

const int list = 1 << 10;
map<int, int> t[list * 2 + 1];

void update(map<int, int> &m, int key, int val) {
	if (m.count(key) == 0) m[key] = val; else m[key] = min(m[key], val);
}
int get(map<int, int> &m, int key) {
	if (m.count(key) == 0) return INF; else return m[key];
}

void update(int v, int col, int value) {
	v += list;
	update(t[v], col, value);
	while (v > 1) {
		v >>= 1;
		update(t[v], col, min(get(t[v * 2], col), get(t[v * 2 + 1], col)));
	}
}

int minlr(int l, int r, int col) {
	l += list;
	r += list;
	int res = min(get(t[l], col), get(t[r], col));
	while (l <= r) {
		if (l % 2 == 1) res = min(res, get(t[l], col));
		if (r % 2 == 0) res = min(res, get(t[r], col));
		l = ((l + 1) >> 1);
		r = ((r - 1) >> 1);
	}
	return res;
}

map<int, int> allmap;

void up(map<int, int>& m) {
	for(map<int, int>::iterator i = m.begin(); i != m.end(); ++i) {
		update(allmap, i->first, i->second);
	}
}

void minalllr(int l, int r) {
	l += list;
	r += list;
	while (l <= r) {
		if (l % 2 == 1) up(t[l]);
		if (r % 2 == 0) up(t[r]);
		l = ((l + 1) >> 1);
		r = ((r - 1) >> 1);
	}
}

int solveone(int f, int s) {
	forn(i, list * 2 + 1) t[i].clear();
	update(0, -1, 0);
	forn(i, n) {
		int curc = segs[i].c;
		if (curc == f || curc == s) curc = -1;
		int pr = minlr(segs[i].l, segs[i].r, curc);
		if (curc != -1) {
			pr = min(pr, minlr(segs[i].l, segs[i].r, -1));
		} else {
			allmap.clear();
			minalllr(segs[i].l, segs[i].r);
			for(map<int, int>::iterator q = allmap.begin(); q != allmap.end(); ++q) {
				update(segs[i].r, q->first, q->second + 1);
			}
		}
		if (pr < INF) {
			update(segs[i].r, curc, pr + 1);
		}
	}
	int res = minlr(kl - 1, kl - 1, -1);
	forn(i, nc) {
		res = min(res, minlr(kl - 1, kl - 1, i));
	}
	return res;
}

void solve() {
	vector<int> ps;
	vector<string> ncols;
	ncols = cols;
	norm(ncols);
	forn(i, n) segs[i].c = num(ncols, cols[i]);
	ps.clear();
	forn(i, n) {
		ps.pb(segs[i].l);
		ps.pb(segs[i].r + 1);
	}
	ps.pb(1);
	ps.pb(10001);
	norm(ps);
	kl = (int)ps.size();
	forn(i, n) segs[i].l = num(ps, segs[i].l);
	forn(i, n) segs[i].r = num(ps, segs[i].r + 1);

	ans = INF;
	nc = (int)ncols.size();
	sort(all(segs));
	forn(i, nc) {
		forn(j, i + 1) {
			ans = min(ans, solveone(i, j));
		}
	}
}

int triv() {
	int ans = INF;
	forn(msk, 1 << n) {
		vector<string> cls;
		int k = 0;
		forn(i, n) if (msk & (1 << i)) {
			cls.pb(cols[i]);
			++k;
		}
		norm(cls);
		if (cls.size() > 3) continue;
		bool u[10001];
		memset(u, 0, sizeof u);
		forn(i, n) if (msk & (1 << i)) {
			for(int q = segs[i].l; q <= segs[i].r; ++q) {
				u[q] = true;
			}
		}
		bool ok = true;
		forn(i, 10000) if (!u[1 + i]) {
			ok = false;
		}
		if (!ok) continue;
		ans = min(ans, k);
	}
	return ans;
}

void readdata() {
	cin >> n;
	cols.clear();
	segs.clear();
	forn(i, n) {
		string s;
		int l, r;
		cin >> s >> l >> r;
		cols.pb(s);
		seg cur;
		cur.l = l, cur.r = r;
		segs.pb(cur);
	}
}

int main() {
	//freopen("sample.in", "rt", stdin);
	int tst;
	cin >> tst;
	forn(i, tst) {
		cout << "Case #" << i + 1 << ": ";
		cerr << i + 1 << endl;
		readdata();
		//int triva = triv();
		solve();
		/*if (ans != triva) {
			cerr << "!!!!!!!!!!!!!!!!!!!!! " << i << " " << ans << " " << triva << endl;
			return 0;
		}*/
		outdata();
	}
	return 0;
}

