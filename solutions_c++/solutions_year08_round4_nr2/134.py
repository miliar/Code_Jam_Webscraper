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

int main() {
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    FOR (ntest, 1, test+1) {
		cout << "Case #" << ntest << ": ";
		int n, m, a;
		cin >> n >> m >> a;
		
		for (int x2 = -n; x2 <= n; ++x2)
			for (int y2 = -m; y2 <= m; ++y2)
				for (int x3 = -n; x3 <= n; ++x3)
					for (int y3 = -m; y3 <= m; ++y3) {
						int minx = x2 <? x3 <? 0;
						int miny = y2 <? y3 <? 0;
						
						if (x2 - minx <= n && y2 - miny <= m && 
							x3 - minx <= n && y3 - miny <= m &&
							abs (x2 * y3 - x3 * y2) == a
							) {
								cout << (x2 - minx) << ' ' << (y2 - miny) << ' ' << (x3 - minx) << ' ' << (y3 - miny) << ' ' << (-minx) << ' ' << (-miny);
								goto next;
							}								
								
					}
		cout << "IMPOSSIBLE";
next:	cout << endl;
	}    
	return 0;
}
