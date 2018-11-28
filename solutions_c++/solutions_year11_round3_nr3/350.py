#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define TRACE(x) cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x) cerr << #x << " = " << x << endl;

typedef long long ll;
typedef long double ld;
typedef unsigned long ulong;
typedef unsigned long long ull;

int tnum;
string s;
int a[100];

int main() {
	cin >> tnum;
	REP(ti,tnum) {
		int n, l, h;
		cin >> n >> l >> h;
		REP(i,n)
			cin >> a[i];
		int ans = -1;
		for (int x = l; x <= h; ++x) {
			bool fail = false;
			REP(i,n)
				if (x % a[i] == 0 || a[i] % x == 0)
					;
				else {
					fail = true;
					break;
				}
			if (!fail) {
				ans = x;
				break;
			}
		}
		if (ans == -1)
			printf("Case #%d: NO\n", 1LL+ti);
		else
			printf("Case #%d: %d\n", 1LL+ti, ans);

	}
	return 0;
}