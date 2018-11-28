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
char a[50][50];

int main() {
	cin >> tnum;
	REP(ti,tnum) {
		int r, c;
		cin >> r >> c;
		REP(i,r) {
			cin >> s;
			REP(j,c)
				a[i][j] = s[j];
		}
		REP(i,r-1)
			REP(j,c-1)
				if (a[i][j] == '#' && a[i+1][j] == '#'
					&& a[i][j+1] == '#' && a[i+1][j+1] == '#') {
					a[i][j] = '/';
					a[i+1][j] = '\\';
					a[i][j+1] = '\\';
					a[i+1][j+1] = '/';
				}
		printf("Case #%d:\n", 1LL+ti);
		bool fail = false;
		REP(i,r)
			REP(j,c)
				if (a[i][j] == '#')
					fail = true;
		if (fail) {
			puts("Impossible");
			continue;
		}
		REP(i,r) {
			REP(j,c)
				putchar(a[i][j]);
			putchar('\n');
		}
	}
	return 0;
}