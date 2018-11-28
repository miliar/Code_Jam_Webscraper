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
	int t, tm;
	int DEBUG = 0;
	
	cin >> t;
	
	REP(i,t){ 
		int n, s, p, sp;
		int ans = 0;
		VI t;
		cin >> n >> s >> p;
		REP(k,n){
			cin >> tm;
			t.PB(tm);
		}
		SORT(t);

		sp = s;
		if(DEBUG) cout << "DEBUG Case #" << (i+1) << endl;

		REP(k,n){
			int z = t[k] / 3;
			if(DEBUG){
				cout << "DEBUG " << t[k] << " / 3 = " << z << endl;
			}
			if ( z * 3 == t[k] ) {
				if ( z >= p ) {
					ans++;
					if(DEBUG) cout << "DEBUG splitted " << z << " " << z << " " << z << endl;
					if(DEBUG) cout << "DEBUG GOT" << endl;
				} else if ( s > 0 && z + 1 >= p && z-1 >= 0 ) {
					// surprised
					ans++;
					s--;
					if(DEBUG) cout << "DEBUG sprised. " << z-1 << " " << z << " " << z+1 << endl;
					if(DEBUG) cout << "DEBUG GOT" << endl;
				} else {
					if(DEBUG) cout << "DEBUG splitted " << z << " " << z << " " << z << endl;
				}
			} else {
				if ( z*3 + 1 == t[k] ) {
					if(DEBUG) cout << "DEBUG splitted " << z << " " << z << " " << z+1 << endl;
					if ( z >= p || z + 1 >= p ) {
						ans++;
						if(DEBUG) cout << "DEBUG GOT" << endl;
					}
				} else if ( z*3 + 2 == t[k] ) {
					if ( z >= p || z + 1 >= p ) {
						ans++;
						if(DEBUG) cout << "DEBUG splitted " << z << " " << z+1 << " " << z+1 << endl;
						if(DEBUG) cout << "DEBUG GOT" << endl;
					} else if ( z + 2 >= p && s > 0 ) {
						if(DEBUG) cout << "DEBUG sprised. " << z << " " << z << " " << z+2 << endl;
						if(DEBUG) cout << "DEBUG GOT" << endl;
						s--;
						ans++;
					} else {
						if(DEBUG) cout << "DEBUG splitted " << z << " " << z+1 << " " << z+1 << endl;
					}
				}
			}
		}

		cout << "Case #" << (i+1) << ": " << ans << endl;

	}

	return 0;

}