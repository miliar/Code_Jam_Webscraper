#pragma comment(linker, "/STACK:128000000")
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

struct Problem {
	int problemId;
	// problem data
	vector<vi> a;
	vector<vi> d;
	vector<vi> d1;
	vector<vi> d2;
	vector<vi> d3;
	vector<vi> d4;
	int n, m, D;

	// some data
	int res;

	void read() {
		cin >> n >> m >> D;
		a = vector<vi>(n, vi(m, 0));
		for (int i = 0; i < n; ++i) {
			string s;
			cin >> s;
			for (int j = 0; j < m; ++j)
				a[i][j] = s[j] - '0';
		}
	}

	int get(int x1, int y1, int x2, int y2) {
		++x2, ++y2;
		return d[x2][y2] - d[x1][y2] - d[x2][y1] + d[x1][y1];
	}

	int get1(int x1, int y1, int x2, int y2) {
		++x2, ++y2;
		return d1[x2][y2] - d1[x1][y2] - d1[x2][y1] + d1[x1][y1];
	}

	int get2(int x1, int y1, int x2, int y2) {
		++x2, ++y2;
		return d2[x2][y2] - d2[x1][y2] - d2[x2][y1] + d2[x1][y1];
	}

	int get3(int x1, int y1, int x2, int y2) {
		++x2, ++y2;
		return d3[x2][y2] - d3[x1][y2] - d3[x2][y1] + d3[x1][y1];
	}

	int get4(int x1, int y1, int x2, int y2) {
		++x2, ++y2;
		return d4[x2][y2] - d4[x1][y2] - d4[x2][y1] + d4[x1][y1];
	}

	bool check(int x1, int y1, int x2, int y2) {
		int mx = x1 + x2, my = y1 + y2;
		int sx = 0, sy = 0;
		for (int i = x1; i <= x2; ++i)
			for (int j = y1; j <= y2; ++j) {
				if (i == x1 && j == y1) continue;
				if (i == x1 && j == y2) continue;
				if (i == x2 && j == y1) continue;
				if (i == x2 && j == y2) continue;
				sx += (2 * i - mx) * a[i][j];
				sy += (2 * j - my) * a[i][j];
			}
		return sx == 0 && sy == 0;
	}

	void solve() {
		criticalSection.lock();
		cerr << "Solving case " << problemId << "\n";
		criticalSection.unlock();
		d = vector<vi>(n + 1, vi(m + 1, 0));
		d1 = d;
		d2 = d;
		d3 = d;
		d4 = d;
		for (int i = 0; i < n; ++i) {
			int s = 0;
			int s1 = 0;
			int s2 = 0;
			int s3 = 0;
			int s4 = 0;
			for (int j = 0; j < m; ++j) {
				s += a[i][j];
				s1 += a[i][j] * (m - j);
				s2 += a[i][j] * (j + 1);
				s3 += a[i][j] * (n - i);
				s4 += a[i][j] * (i + 1);
				d[i + 1][j + 1] = d[i][j + 1] + s;
				d1[i + 1][j + 1] = d1[i][j + 1] + s1;
				d2[i + 1][j + 1] = d2[i][j + 1] + s2;
				d3[i + 1][j + 1] = d3[i][j + 1] + s3;
				d4[i + 1][j + 1] = d4[i][j + 1] + s4;
			}
		}

		res = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				for (int k = 3; i + k <= n && j + k <= m; ++k) {
					int coef = k / 2;
					int s1, s2;
					int x = i + (k - 1) / 2, y = j + (k - 1) / 2;
					int X = i + k / 2, Y = j + k / 2;
					s1 = get3(i, j, x, j + k - 1) - get(i, j, x, j + k - 1) * (n - i - coef);
					s2 = get4(X, j, i + k - 1, j + k - 1) - get(X, j, i + k - 1, j + k - 1) * (i + k - coef);
					s1 -= a[i][j] * coef;
					s1 -= a[i][j + k - 1] * coef;
					s2 -= a[i + k - 1][j] * coef;
					s2 -= a[i + k - 1][j + k - 1] * coef;
					if (k % 2 == 0) {
						s1 *= 2, s2 *= 2;
						s1 -= get(i, j, x, j + k - 1);
						s2 -= get(X, j, i + k - 1, j + k - 1);
						s1 += a[i][j];
						s1 += a[i][j + k - 1];
						s2 += a[i + k - 1][j];
						s2 += a[i + k - 1][j + k - 1];
					}
					//if (problemId == 8 && k == 6)
					//	cerr << s1 << " "<< s2 << "\n";
					if (s1 != s2) continue;
					s1 = get1(i, j, i + k - 1, y) - get(i, j, i + k - 1, y) * (m - j - coef);
					s2 = get2(i, Y, i + k - 1, j + k - 1) - get(i, Y, i + k - 1, j + k - 1) * (j + k - coef);
					s1 -= a[i][j] * coef;
					s1 -= a[i + k - 1][j] * coef;
					s2 -= a[i][j + k - 1] * coef;					
					s2 -= a[i + k - 1][j + k - 1] * coef;
					if (k % 2 == 0) {
						s1 *= 2, s2 *= 2;
						s1 -= get(i, j, i + k - 1, y);
						s2 -= get(i, Y, i + k - 1, j + k - 1);
						s1 += a[i][j];
						s1 += a[i + k - 1][j];
						s2 += a[i][j + k - 1];
						s2 += a[i + k - 1][j + k - 1];
					}
					if (s1 != s2) continue;
					//if (!check(i, j, i + k - 1, j + k - 1)) continue;
					res = max(res, k);
				}
		d.clear();
		a.clear();
		cerr << res << "\n";
		cerr.flush();
	}

	void save() {
		if (res == 0) cout << "IMPOSSIBLE\n";
		else cout << res << "\n";
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
