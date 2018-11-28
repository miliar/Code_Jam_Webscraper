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

const int maxn = 1100;

double d[maxn];

struct Problem {
	int problemId;
	// problem data
	int n;
	// some data
	double res;

	void read() {
		int m;
		cin >> m;
		n = 0;
		for (int i = 0; i < m; ++i) {
			int x;
			cin >> x;
			if (x != i + 1)
				++n;
		}
	}

	void solve() {
		criticalSection.lock();
		cerr << "Solving case " << problemId << "\n";
		criticalSection.unlock();
		res = d[n];
	}

	void save() {
		printf("%.10lf\n", res);
	}
};

//double C[maxn][maxn];

void precalc() {
	/*memset(C, 0, sizeof(C));
	C[0][0] = 1.0;
	for (int i = 1; i < maxn; ++i) {
		C[i][0] = 1.0;
		for (int j = 1; j < maxn; ++j) {
			C[i][j] = C[i - 1][j] + C[i - 1][j - 1];
		}
	}*/
	double fact[maxn];
	fact[0] = 1.0;
	for (int i = 1; i < maxn; ++i)
		fact[i] = fact[i - 1] / (i + 0.0);
	double f[maxn];
	f[0] = 1.0;
	for (int i = 1; i < maxn; ++i) {
		f[i] = 0.0;
		double cur = 1.0;
		for (int j = 0; j <= i; ++j) {
			if (j % 2 == 0) f[i] += cur;
			else f[i] -= cur;
			cur /= (j + 1.);
		}
	}
	d[0] = 0.0;
	for (int i = 1; i < maxn; ++i) {
		double alpha = f[i];
		double cur = 0.0;
		for (int j = 1; j <= i; ++j)
			cur += fact[j] * f[i - j] * d[i - j];
		cur += 1.0;
		cur /= 1. - alpha;
		d[i] = cur;
	}
}

int main()
{
	//freopen("", "r", stdin);
	//freopen("", "w", stdout);
	precalc();
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
