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

const double eps = 1E-12;

struct Problem {
	int problemId;
	// problem data
	int n;
	double L, S, R, T;
	vector<pair<pair<double, double>, double> > v;

	// some data
	double res;

	void read() {
		cin >> L >> S >> R >> T >> n;
		v.resize(n);
		for (int i = 0; i < n; ++i)
			cin >> v[i].first.first >> v[i].first.second >> v[i].second;
		sort(all(v));
		vector<pair<pair<double, double>, double> > w;
		double prev = 0.0;
		for (int i = 0; i < sz(v); ++i) {
			if (v[i].first.first > prev + eps) {
				w.pb(mp(mp(prev, v[i].first.first), 0.0));
			}
			w.pb(v[i]);
			prev = v[i].first.second;
		}
		if (prev < L - eps)
			w.pb(mp(mp(prev, L), 0.0));
		v = w;
		sort(all(v), [&](pair<pair<double, double>, double> p, pair<pair<double, double>, double> q) { return p.second < q.second; });		
		w.clear();
		for (int i = 0; i < sz(v); ++i) {
			if (T < eps) {
				w.pb(v[i]);
				continue;
			}
			double t0 = (v[i].first.second - v[i].first.first) / (v[i].second + R);
			if (t0 < T + eps) {
				T -= t0;
				v[i].second += R - S;
				w.pb(v[i]);
				continue;
			}
			double x = v[i].first.first + (v[i].second + R) * T;
			T = 0.0;
			w.pb(mp(mp(v[i].first.first, x), v[i].second + R - S));
			w.pb(mp(mp(x, v[i].first.second), v[i].second));
		}
		v = w;
		sort(all(v));
		res = 0.0;
		for (int i = 0; i < sz(v); ++i)
			res += (v[i].first.second - v[i].first.first) / (v[i].second + S);
	}

	void solve() {
		criticalSection.lock();
		cerr << "Solving case " << problemId << "\n";
		criticalSection.unlock();
	}

	void save() {
		printf("%.20lf\n", res);
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

	parallel_for_each(all(problems), 
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
