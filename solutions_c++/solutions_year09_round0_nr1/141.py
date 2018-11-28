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

bool can[15][256];

int main() {
	int l, d, n;
	cin >> l >> d >> n;
	vector<string> dict(d);
	FOR(i, 0, d) cin >> dict[i];
	FOR(i, 0, n) {
		SET(can, false);
		string s;
		cin >> s;
		int pos = 0;
		FORE(j, s) {
			if (s[j] == '(') {
				for (++j; s[j] != ')'; ++j) can[pos][s[j]] = true;
			}
			else can[pos][s[j]] = true;
			++pos;
		}
		int res = 0;
		FORE(j, dict) {
			string cur = dict[j];
			FORU(k, 0) {
				if (k == cur.size()) {
					++res;
					break;
				}
				if (!can[k][cur[k]]) break;
			}
		}
		cout << "Case #" << i+1 << ": " << res << endl;
	}
}
