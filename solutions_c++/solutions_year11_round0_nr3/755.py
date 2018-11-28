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

int main() {
	int tnum;
	cin >> tnum;
	REP(ti,tnum) {
		int n;
		cin >> n;
		int m = 1e7;
		int sum = 0;
		int xsum = 0;
		int x;
		REP(i,n) {
			cin >> x;
			sum += x;
			m = min(m, x);
			xsum ^= x;
		}
		if (xsum == 0)
			printf("Case #%d: %d\n", ti+1, sum-m);
		else
			printf("Case #%d: NO\n", ti+1);
	}
	return 0;
}

