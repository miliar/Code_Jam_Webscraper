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
	vector<ii> v;

	// some data
	int res;

	void read() {
		cin >> n;
		for (int i = 0; i < n; ++i) {
			string s;
			int x, y;
			cin >> s >> y;
			x = s == "O" ? 0 : 1;
			v.pb(ii(x, y));
		}
	}

	void solve() {
		criticalSection.lock();
		cerr << "Solving case " << problemId << "\n";
		criticalSection.unlock();
		
		int T[2] = {0, 0};
		int pos[2] = {1, 1};
		
		for (int i = 0; i < n; ++i) {
			int x = v[i].first, y = v[i].second;
			T[x] += abs(pos[x] - y);
			pos[x] = y;
			T[x] = max(T[x], T[1 - x]);
			++T[x];
		}
		res = max(T[0], T[1]);		
	}

	void save() {
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
