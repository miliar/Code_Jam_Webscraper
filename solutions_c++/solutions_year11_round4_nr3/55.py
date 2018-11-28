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

vi vp;

const int maxn = 1000 * 1000 * 2;

bitset<maxn> u;

struct Problem {
	int problemId;
	// problem data
	int64 n;

	// some data
	int64 res;

	void read() {
		cin >> n;
	}

	void solve() {
		criticalSection.lock();
		cerr << "Solving case " << problemId << "\n";
		criticalSection.unlock();
		res = 1;
		for (int i = 0; i < sz(vp); ++i) {
			int64 x = vp[i];
			if (x * x > n) break;
			int64 y = n;
			int deg = 0;
			while (y >= x) y /= x, ++deg;
			res += max(0, deg - 1);
		}
		if (n == 1) res = 0;
	}

	void save() {
		cout << res << "\n";
	}
};

int main()
{
	u[0] = 1;
	u[1] = 1;
	for (int i = 2; i * i <= maxn; ++i) {
		if (u[i]) continue;
		for (int j = i * i; j < maxn; j += i)
			u[j] = 1;
	}
	for (int i = 2; i < maxn; ++i)
		if (!u[i]) vp.pb(i);
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
