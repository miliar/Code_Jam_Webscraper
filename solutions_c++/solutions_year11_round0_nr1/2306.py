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
		int N; cin >> N;

		vi pos(2,1), last(2,0);
		int tm = 0;

		for(int i = 0; i < N; ++i) {
			string s; int b;
			cin >> s >> b;

			int k = (s[0] == 'O' ? 0 : 1);

			int need = 1 + max(0, abs(pos[k] - b) - (tm - last[k]));
			tm += need;

			pos[k] = b;
			last[k] = tm;
		}

		cout << "Case #" << t << ": " << tm << "\n";
	}



	return 0;
}
