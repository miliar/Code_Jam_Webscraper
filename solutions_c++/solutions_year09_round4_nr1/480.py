#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

template <class A, class B> void CONV(A& x, B& y) { stringstream s; s << x; s >> y; }
typedef long long LL;
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORE(i, v) FOR(i, 0, v.size())
#define FORU(i, a) for (int i = a; ; ++i)
#define SORT(v) sort(v.begin(), v.end())
#define SET(a, n) memset(a, n, sizeof a)

int main() {
	int t;
	cin >> t;
	FOR(i, 0, t) {
		int n;
		cin >> n;
		cin.get();
		vector<string> grid(n);
		FOR(j, 0, n) getline(cin, grid[j]);
		vector<int> v(n);
		FORE(j, grid) {
			v[j] = 0;
			FORE(k, grid[j]) {
				if (grid[j][k] == '1') v[j] = k;
			}
		}
		int res = 0;
		FORE(j, v) {
			int pos = j;
			while (v[pos] > j) ++pos;
			while (pos != j) {
				swap(v[pos], v[pos-1]);
				--pos;
				++res;
			}
		}
		cout << "Case #" << i+1 << ": " << res << endl;
		/*
		for(;;) {
			int best = -1;
			FORE(j, v) {
				if (v[j] <= j) continue;
				if (best == -1 || v[j] >= v[best]) best = j;
			}
			//cout << best << ' ' << v[best] << endl;
			if (best == -1) {
               	cout << "Case #" << i+1 << ": " << res << endl;
               	break;
			}
			while (v[best] > best) {
				swap(v[best], v[best+1]);
				++best;
				++res;
			}
			FORE(j, v) cout << v[j] << endl;
			system("pause");
		}
		*/
	}
}
