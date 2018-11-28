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

map< pair <int, int>, int> mm;

void main() {
	int T;
	int i, j, k, m;

	cin >> T;

	REP(i, T) {
		int A, B;
		char buf[50];
		cin >> A >> B;
		int res = 0;
		mm.clear();

		for (j = A; j <= B; ++j) {
			sprintf(buf, "%d", j);
			int x = strlen(buf);

			for (k = 1; k <= x - 1; ++k) {
				char tmp = buf[x - 1];
				for (m = x - 2; m >= 0; --m) {
					buf[m + 1] = buf[m];
				}
				buf[0] = tmp;

				if (buf[0] == '0')
					continue;

				int nj = atoi(buf);

				if (j < nj && nj <= B && A <= nj) {
					++mm[make_pair(j, nj)];
					int ps = mm[make_pair(j, nj)];
					if (ps == 1)
						++res;
				}
			}
		}

		cout << "Case #" << (i+1) << ": " << res << endl;
	}
}