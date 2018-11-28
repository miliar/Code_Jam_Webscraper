#pragma comment(linker, "/STACK:256000000")
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
	int a[300][300];
	int op[300][300];
	string s;

	// some data
	vector<char> res;

	void read() {
		memset(a, -1, sizeof(a));
		memset(op, -1, sizeof(op));
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i) {
			string t;
			cin >> t;
			a[t[0]][t[1]] = t[2];
			a[t[1]][t[0]] = t[2];
		}
		cin >> n;
		for (int i = 0; i < n; ++i) {
			string t;
			cin >> t;
			op[t[0]][t[1]] = 1;
			op[t[1]][t[0]] = 1;
		}
		cin >> n;
		cin >> s;
	}

	void solve() {
		criticalSection.lock();
		cerr << "Solving case " << problemId << " " << s << "\n";
		criticalSection.unlock();
		vector<char> v;
		for (int i = 0; i < sz(s); ++i) {
			v.pb(s[i]);
			if (sz(v) >= 2) {
				char c = a[v[sz(v) - 1]][v[sz(v) - 2]];
				if (c != -1) {
					v.pop_back();
					v.pop_back();
					v.pb(c);
				}
			}
			
			char cur = v[sz(v) - 1];
			for (int i = 0; i < sz(v); ++i) {
				if (op[v[i]][cur] != -1) {
					v.clear();
					break;
				}
			}
		}
		res = v;
	}

	void save() {
		printf("[");
		for (int i = 0; i < sz(res); ++i) {
			if (i) printf(", ");
			printf("%c", res[i]);
		}
		printf("]\n");
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
