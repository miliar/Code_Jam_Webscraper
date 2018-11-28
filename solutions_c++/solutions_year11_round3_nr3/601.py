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
	int t;
	int N, L, H;
	int tmp, ans;
	int imp;
	VI others;

	cin >> t;
	REP(i,t){
		imp = 0;
		others.clear();

		cin >> N >> L >> H;
		REP(k,N){
			cin >> tmp;
			others.PB(tmp);
		}

		FOR(f,L,H+1){
			imp = 0;
			REP(k,others.size()){
				if ( f % others[k] != 0 && others[k] % f != 0 ) {
					imp = 1; break;
				}
			}
			if ( imp == 0 ) {
				ans = f; break;	
			}
		}

		cout << "Case #" << (i+1) << ": ";
		if ( imp == 1 ) {
			cout << "NO" << endl;
		} else {
			cout << ans << endl;
		}

	}

	return 0;

}