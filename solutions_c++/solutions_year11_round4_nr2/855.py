// Some algorithmic problem solution by Artem Khizha [DNU2] (also known as metar)

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

int r, c;
int m[500][500];

bool check(int x, int y, int k) {
	ld xc = x + (k-1)/2.0;
	ld yc = y + (k-1)/2.0;
	ld ax = 0.0;
	ld ay = 0.0;
	ax -= (x-xc)*m[x][y] + (x-xc)*m[x][y+k-1] +(x+k-1-xc)*m[x+k-1][y]  + (x+k-1-xc)*m[x+k-1][y+k-1];
	ay -= (y-yc)*m[x][y] + (y+k-1-yc)*m[x][y+k-1] + (y-yc)*m[x+k-1][y] + (y+k-1-yc)*m[x+k-1][y+k-1];
	for (int i = x; i < x+k; ++i)
		for (int j = y; j < y+k; ++j) {
			ay += (j-yc)*m[i][j];
			ax += (i-xc)*m[i][j];
		}
	return (ax == 0) && (ay == 0);
}

int main() {
	int tnum;
	cin >> tnum;
	REP(ti,tnum) {
		int d;
		cin >> r >> c >> d;
		string s;
		REP(i,r) {
			cin >> s;
			REP(j,c)
				m[i][j] = s[j]-'0'+d;
		}
		int ans = 0;
		REP(i,r)
			REP(j,c) {
				for (int k = 3; k <= min(r-i, c-j); ++k) {
					if (check(i, j, k)) {
						ans = max(ans, k);
					}
				}
			}
		if (ans >= 3)
			printf("Case #%d: %d\n", 1+ti, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", 1+ti);
	}
	return 0;
}