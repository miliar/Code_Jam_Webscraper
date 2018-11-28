#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <utility>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define REP(i,n) FOR(i,0,n)
#define REPD(i,n) FORD(i,0,n)
#define VAR(v,w) __typeof(w) v=(w)
#define FORE(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define PB push_back
#define ALL(c) (c).begin(),(c).end()
#define SIZE(c) ((int)(c).size())
#define MP make_pair
#define FT first
#define SD second
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<double> VD;
typedef vector<LD> VLD;
typedef vector<LL> VLL;
typedef vector<bool> VB;
typedef istringstream ISS;
typedef ostringstream OSS;

int main() {
	int ccc;
	cin >> ccc;
	REP(cc,ccc) {
		int n, m, a;
		cin >> n >> m >> a;
		REP(x1,n+1) REP(x2,n+1) REP(y1,m+1) REP(y2,m+1) {
			if (x1*y2-x2*y1 == a) {
				cout << "Case #" << cc+1 << ": 0 0 " << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
				goto next;
			}
		}
		cout << "Case #" << cc+1 << ": IMPOSSIBLE" << endl;
next:;
	}
}
