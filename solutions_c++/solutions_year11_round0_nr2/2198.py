/*
 * GCJ 2011 qualifying
 */
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <cmath>
#include <iomanip>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long LL;

template<typename T> inline int sz(const T& x) { return (int)x.size(); }


int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int T; cin >> T;
	for(int t = 1; t <= T; ++t) {
		vvi comb(256, vi(256,0));
		vvi opposed(comb);

		int C; cin >> C;
		while(C--) {
			string s; cin >> s;
			comb[s[0]][s[1]] = (int)s[2];
			comb[s[1]][s[0]] = (int)s[2];
		}

		int D; cin >> D;
		while(D--) {
			string s; cin >> s;
			opposed[s[0]][s[1]] = 1;
			opposed[s[1]][s[0]] = 1;
		}

		int N; cin >> N;
		string s; cin >> s;

		vi res;

		for(int i = 0; i < N; ++i) {
			res.push_back( s[i] );

			while( sz(res) > 1  &&  comb[res[sz(res)-1]][res[sz(res)-2]] ) {
				int x = comb[res[sz(res)-1]][res[sz(res)-2]];
				res.pop_back(); res.pop_back();
				res.push_back(x);
			}

			for(int j = 0; j < sz(res)-1; ++j) {
				if( opposed[res[j]][res.back()] )
					res.clear();
			}
		}

		cout << "Case #" << t << ": [";

		if( sz(res) )
			cout << (char)res[0];

		for(int i = 1; i < sz(res); ++i)
			cout << ", " << (char)res[i];

		cout << "]\n";
	}



	return 0;
}
