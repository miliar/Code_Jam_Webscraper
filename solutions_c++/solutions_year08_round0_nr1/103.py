#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define pb push_back

#define VAR(a,b) __typeof(b) a=(b)
#define FORE(it,a) for(VAR(it,(a).begin());it!=(a).end();it++)
#define X first
#define Y second
#define DEBUG(x) cout << #x << " = " << x << endl;

#define INF 1000000000

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef pair <int, VI> PIVI;
typedef long long ll;

char ss[100000];
int d[1001][101];

int main() {
    freopen("a-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
	gets (ss);
	int t;
	sscanf (ss, "%d", &t);	
	REP (test, t) {
		int n, m;
		vector <string> a;
		vector <string> b;		
		gets (ss);
		sscanf (ss, "%d", &n);
		REP (i, n) {
			gets (ss);
			a.pb ((string) ss);
		}		
		gets (ss);		
		sscanf (ss, "%d", &m);
		REP (i, m) {
			gets (ss);
			b.pb ((string) ss);
		}	
		
		REP (i, m+1)
			REP (j, n+1)
				d[i][j] = INF;
				
		REP (j, n+1)
			d[0][j] = 0;
							
		REP (i, m) {
			REP (j, n)
				if (a[j] != b[i])
					d[i+1][j] <?= d[i][j];
				else
					REP (k, n)
						if (k != j)
							d[i+1][k] <?= d[i][j] + 1;
		}
		
		int res = INF;
		REP (i, n)
			res <?= d[m][i];
		
		printf ("Case #%d: %d\n", test+1, res);
	}
	return 0;
}
