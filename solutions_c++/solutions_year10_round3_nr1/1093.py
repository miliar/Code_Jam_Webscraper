#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define GI ({int _t; scanf("%d", &_t); _t;})
#define FOR(i, a, b) for (int i=a; i<b; i++)
#define REP(i, a) FOR(i, 0, a)
#define DBG(x) cout << #x << "::" << x << endl;
#define DBGV(_v) { FOR(_i, 0, _v.size()) { cout << _v[_i] << "\t";} cout << endl;}
#define sz size()
#define pb push_back

int main() {
	int kases = GI;
	for(int kase = 1; kase <= kases; kase++) {
		vector <int> a, b;
		
		int n = GI, t;
		REP(i, n) {
			t = GI;
			a.pb(t);
			t = GI;
			b.pb(t);
		}
		int res = 0;
		REP(i, n) {
			REP(j, n) {
				if ((a[i] > a[j] && b[i] < b[j])) {
					res++;
				}
			}
		}
		printf("Case #%d: %d\n", kase, res);
	}
}
