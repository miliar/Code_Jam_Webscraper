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
#include <complex>

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
#define FOREACH(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define LOOP for(;;)
#define zero(n) memset((n),0,sizeof(n))
#define RMB(x) (x).erase((x).begin())
#define RME(x) (x).pop_back()
#define SORT(x) sort((x).begin(),(x).end())
#define REVERSE(x) reverse((x).begin(),(x).end())
#define PB push_back
#define ISS istringstream
#define OSS ostringstream


int main ( void )
{
	ll t, pd, pg, n;
	int flag;
	cin >> t;

	REP(i,t){
		cin >> n >> pd >> pg;
		ll ppd = pd, cnt = 1;
		ll pgd = pg, cnt2 = 1;

		while ( ppd % 100 != 0 ) { ppd += pd; cnt++; }
		while ( pgd % 100 != 0 ) { pgd += pg; cnt2++; }

		// cout << cnt << endl;
		// cout << cnt2 << endl;

		flag = 0;
		for ( ll j = cnt; j <= n; j+=cnt ) {
			ll k = cnt2;
			while ( 1 ) {
				ll nk = k;
				k += cnt2;

				if ( nk < j ) continue;
				if ( (nk * pg) / 100 < (j * pd) / 100 ) {
					if ( nk > 20000000 ) {
						flag = 2; break;
					}
					continue;
				}

				ll totalwin = ( nk * pg ) / 100;
				ll todaywin = ( j * pd ) / 100;

				if ( ( nk - j ) < totalwin - todaywin ) {
					if ( nk > 20000000 ) {
						flag = 2; break;
					}
					continue;
				}

				flag = 1;
				break;

			}
			if ( flag == 1 || flag == 2 ) break;

		}

		if ( flag == 1 ) {
			cout << "Case #" << (i+1) << ": Possible" << endl;
		} else if ( flag == 2 || flag == 0 ) {
			cout << "Case #" << (i+1) << ": Broken" << endl;
		}

	}

	return 0;

}