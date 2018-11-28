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
	int el[1002];
	bool sett[1002];

	REP(i,n) {
		cin >> m;
		int res = 0;
		memset(sett,0x00,sizeof(sett));
		REP(j,m) {
			cin >> el[j];
		}

		REP(j,m) {
			if (sett[j])
				continue;

			sett[j] = true;
			if (j+1 == el[j])
				continue;

			int cyc = 2;
			int next = el[j];
			sett[next - 1] = true;
			while (el[next - 1] != j + 1) {
				next = el[next - 1];
				sett[next - 1] = true;
				++cyc;
			}

			res += cyc;
		}

		cout << "Case #" << i + 1 << ": " << res << ".000000" << endl;
	}
}