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

bool g[10010], c[10010], v[10010];
int res0[10010], res1[10010];
const int inf = 1000000000;

int main() {
	int ccc;
	cin >> ccc;
	REP(cc,ccc) {
		int m;
		bool vv;
		cin >> m >> vv;
		FOR(i,1,m+1) {
			if (i <= ((m-1)>>1))
				cin >> g[i] >> c[i];
			else
				cin >> v[i];
		}
		FOR(i,((m-1)>>1)+1,m+1)
			if (v[i]) {
				res0[i] = inf;
				res1[i] = 0;
			} else {
				res0[i] = 0;
				res1[i] = inf;
			}
		FORD(i,1,((m-1)>>1)+1) {
			int a = i << 1;
			int b = a + 1;
			if (g[i]) {
				res0[i] = (res0[a] + res0[b])<?inf;
				res0[i] <?= (res0[a] + res1[b])<?inf;
				res0[i] <?= (res1[a] + res0[b])<?inf;
				res1[i] = (res1[a] + res1[b])<?inf;
			} else {
				res0[i] = (res0[a] + res0[b])<?inf;
				res1[i] = (res0[a] + res1[b])<?inf;
				res1[i] <?= (res1[a] + res0[b])<?inf;
				res1[i] <?= (res1[a] + res1[b])<?inf;
			}
			if (c[i]) {
				if (g[i]) {
					res0[i] <?= (res0[a] + res0[b] + 1)<?inf;
					res1[i] <?= (res0[a] + res1[b] + 1)<?inf;
					res1[i] <?= (res1[a] + res0[b] + 1)<?inf;
					res1[i] <?= (res1[a] + res1[b] + 1)<?inf;
				} else {
					res0[i] <?= (res0[a] + res0[b] + 1)<?inf;
					res0[i] <?= (res0[a] + res1[b] + 1)<?inf;
					res0[i] <?= (res1[a] + res0[b] + 1)<?inf;
					res1[i] <?= (res1[a] + res1[b] + 1)<?inf;
				}
			}
		}
		int res = vv ? res1[1] : res0[1];
		cout << "Case #" << cc+1 << ": ";
		if (res >= inf)
			cout << "IMPOSSIBLE";
		else
			cout << res;
		cout << endl;
	}
}
