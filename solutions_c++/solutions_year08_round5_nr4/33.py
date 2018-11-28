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

int res[110][110];
bool bad[110][110];

int main() {
	int ccc;
	cin >> ccc;
	REP(cc,ccc) {
		int n, m, r;
		cin >> n >> m >> r;
		REP(i,n) REP(j,m) res[i][j] = bad[i][j] = 0;
		REP(rr,r) {
			int a, b;
			cin >> a >> b;
			bad[a-1][b-1] = 1;
		}
		if (!bad[n-1][m-1])
			res[n-1][m-1] = 1;
		REPD(i,n) REPD(j,m) if ((i < n-1 || j < m-1) && !bad[i][j]) {
			int x = 0;
			if (i < n-1 && j < m-2)
				x += res[i+1][j+2];
			if (i < n-2 && j < m-1)
				x += res[i+2][j+1];
			res[i][j] = x % 10007;
		}
		cout << "Case #" << cc+1 << ": " << res[0][0] << endl;
	}
}
