#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <ctime>
#include <sstream>
#include <iomanip>
#include <map>
#include <set>

using namespace std;

typedef vector<int> VI;
typedef vector< vector< int > > VVI;
typedef vector<string> VS;
typedef set<int> SI;
typedef set<string> SS;
typedef long long ll;
typedef unsigned long long ull;

#define REP(i,n) for(int i=0;i<(n);++i)
#define DREP(i,n) for(int i=(n)-1;i>=0;--i)
#define FOR(i,n,m) for(int i=(n);i<(m);++i)
#define DFOR(i,n,m) for(int i=(n);i>=(m);--i)
#define LOOP for(;;)
#define zero(n) memset((n),0,sizeof(n))
#define RMB(x) (x).erase((x).begin())
#define RME(x) (x).erase((x).end()-1)
#define SORT(x) sort((x).begin(),(x).end())
#define PB push_back
#define ISS istringstream
#define OSS ostringstream


int memo[1000][1000];
int memo2[1000][1000];

int main()
{
	int t; cin >> t;
	REP ( i, t ) {
		int n; cin >> n;
		REP ( k, 1000 ) { REP ( l, 1000 ) { memo[k][l] = 0; } }

		int maxy = 0, maxx = 0;

		REP ( j, n ) {
			int x1, x2, y1, y2; cin >> x1 >> y1 >> x2 >> y2;
			FOR ( z, x1, x2+1 ) {
				FOR ( y, y1, y2+1 ) {
					memo[y][z] = 1;
					if ( maxy < z ) maxy = z;
					if ( maxx < y ) maxx = y;
				}
			}
		}



		int ans = 0;
		int flag = 0;
		LOOP {
			flag = 0;
			REP ( x, maxx+1 ) {
				REP ( y, maxy+1 ) {
					if ( memo[x][y] == 1 && memo[x-1][y] != 1 && memo[x][y-1] != 1 ) {
						memo2[x][y] = 0;
					} else if ( memo[x][y] == 0 && memo[x-1][y] == 1 && memo[x][y-1] == 1 ) {
						memo2[x][y] = 1;
					} else {
						memo2[x][y] = memo[x][y];
					}
					if ( memo2[x][y] == 1 ) flag = 1;
				}
				maxy++;
			}
			maxx++;
			memcpy(memo,memo2,sizeof(memo));

			ans++;
			if ( flag == 0 ) break;
		}

		cout << "Case #" << i+1 << ": " << ans << endl;

	}
	
	return 0;

}