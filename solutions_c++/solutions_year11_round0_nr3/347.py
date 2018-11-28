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
	int n;
	vi v;

	// some data
	int64 res;
	int hor;

	void read() {
		cin >> n;
		v.resize(n);
		for (int i = 0; i < n; ++i)
			cin >> v[i];
	}

	void solve() {
		//criticalSection.lock();
		//cerr << "Solving case " << problemId << "\n";
		//criticalSection.unlock();
		int64 sum = 0;
		hor = 0;
		int me = v[0];
		for (int i = 0; i < n; ++i) {
			hor ^= v[i];
			sum += v[i];
			me = min(me, v[i]);
		}
		res = sum - me;
	}

	void save() {
		if (hor)
			cout << "NO\n";
		else
			cout << res << "\n";
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
