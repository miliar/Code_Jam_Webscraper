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

int calc[16][16];
int end[16][16];

int d[1<<16][16];

int main() {
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
	int k;
	string s;
    FOR (ntest, 1, test+1) {
		cout << "Case #" << ntest << ": ";
		cin >> k;
		cin >> s;		
		memset (calc, 0, sizeof (calc));
		
		REP (i, SZ (s))
			REP (j, k)
				calc[i % k][j] += (s[i] != s[(i / k) * k + j]);
		
		memset (end, 0, sizeof (end));
		
		REP (i, SZ (s) - k)
			REP (j, k)
				end[i % k][j] += (s[i] != s[(i / k) * k + k + j]);
				

		int ans = INF;
		REP (start, k) {
			memset (d, 0, sizeof (d));
			REP (i, 1<<16)
				REP (j, 16)
					d[i][j] = INF;
			d[1<<start][start] = 0;
			
			REP (mask, 1<<k)
				REP (j, k) 
					REP (q, k)
						if (!(mask & (1<<q)))
							d[mask | (1<<q)][q] <?= d[mask][j] + calc[j][q];

			REP (j, k)
				ans <?= d[(1<<k)-1][j] + end[j][start];
		}		
		cout << (ans+1);
		cout << endl;
	}    
	return 0;
}
