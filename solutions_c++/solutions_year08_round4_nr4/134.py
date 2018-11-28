#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz size()
#define iss istringstream
#define oss ostringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vs vector<string>

using namespace std;

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int tests;
	cin >> tests;
	fr(test, tests) {
		int k;
		string s;
		cin >> k;
		cin >> s;
		vi p;
		fr(i, k) p.pb(i);
		int ans = beg;
		do {
		//	fr(i, p.sz) cout << p[i] << " ";
		//	cout << endl;
			int m = s.sz/k;
			string ns = s;
			for(int i = 0; i < m; i++) 
				for(int j = 0; j < k; j++) 
					ns[k*i + j] = s[k*i + p[j]];
			int dist = 0;
			for(int i = 0; i < ns.sz - 1; i++) dist += ns[i] != ns[i + 1];
			ans <?= dist;
		//	cout << ans << ' ' << ns << endl;
		} while(next_permutation(p.begin(), p.end()));
		cout << "Case #" << test + 1 << ": " << ans + 1 << endl;
	}
	return 0;
}
