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


bool isCross(int x1, int x2, int y1, int y2)
{
	if ( ( x1 > x2 && y1 < y2 ) || ( x1 < x2 && y1 > y2 ) ) {
		return true;

	} else {
		return false;

	}

}

int main()
{
	int t;
	int ans;

	cin >> t;

	REP ( i, t ) {
		int N;
		VI va, vb;

		cin >> N;
		REP ( j, N ) {
			int x1, x2;
			cin >> x1 >> x2;
			va.PB ( x1 ); vb.PB ( x2 );
		}

		ans = 0;
		if ( va.size() == 1 ) {
			ans = 0;

		} else {
			REP ( j, N ) {
				FOR ( k, j+1, N ) {
					if ( isCross( va[j], va[k], vb[j], vb[k] ) == true ) ans++;

				}
			
			}

		}

		cout << "Case #" << i+1 << ": " << ans << endl;

	}

	return 0;

}