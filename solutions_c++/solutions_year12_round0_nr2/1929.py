#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

void main() {
	int T, N, S, p;
	int t[102];

	cin >> T;

	int i,j;

	REP(i,T) {
		cin >> N >> S >> p;

		int res = 0;
		int pos = S;

		REP(j,N) {
			cin >> t[j];

			if (t[j] % 3 == 0) {
				if (t[j] / 3 >= p) {
					++res;
					continue;
				}

				if (pos > 0 && t[j] / 3 >= 1 && t[j] / 3 <= 9 && t[j] / 3 >= p - 1) {
					--pos;
					++res;
					continue;
				}
			} else if (t[j] % 3 == 1) {
				if (t[j] / 3 >= p - 1) {
					++res;
					continue;
				}

				if (pos > 0 && t[j] / 3 >= 1 && t[j] / 3 <= 9 && t[j] / 3 >= p - 1) {
					--pos;
					++res;
					continue;
				}
			} else {
				if (t[j] / 3 >= p - 1) {
					++res;
					continue;
				}

				if (pos > 0 && t[j] / 3 >= 0 && t[j] / 3 <= 8 && t[j] / 3 >= p - 2) {
					--pos;
					++res;
					continue;
				}
			}
		}

		cout << "Case #" << (i + 1) << ": " << res << endl;
	}
}