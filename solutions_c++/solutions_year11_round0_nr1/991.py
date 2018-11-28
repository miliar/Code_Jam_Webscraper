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
	int n,m;
	int i,j;

	cin >> n;

	REP(i,n) {
		cin >> m;
		char ch;
		int pos;
		int pos1 = 1;
		int pos2 = 1;
		int ti1 = 0;
		int ti2 = 0;

		REP(j,m) {
			cin >> ch >> pos;
			if (ch == 'O') {
				ti1 += abs(pos1 - pos) + 1;
				if (ti1 <= ti2)
					ti1 = ti2 + 1;
				pos1 = pos;
			} else {
				ti2 += abs(pos2 - pos) + 1;
				if (ti2 <= ti1)
					ti2 = ti1 + 1;
				pos2 = pos;
			}
		}

		cout << "Case #" << i + 1 << ": " << max(ti1, ti2) << endl;
	}
}