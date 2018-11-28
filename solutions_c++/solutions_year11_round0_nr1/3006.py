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
	int t, ac, tmp, tm;
	char rbt;
	vector<char> vc;
	vector<int> vi;
	int to, tb;
	int op, bp;
	int am, dtm;

	cin >> t;
	REP(i,t){
		cin >> ac;
		vc.clear(); vi.clear();
		REP(j,ac){
			cin >> rbt >> tmp;
			vc.PB(rbt); vi.PB(tmp);
		}
		
		tb = 0; to = 0; op = 1; bp = 1; tm = 0;
		am = 0;

		REP(j, vc.size()) {
			int nextB = -1, nextO = -1;
			char next = vc[j];
			for ( int z = j; z < vc.size(); z++ ) {
				if ( vc[z]=='O' && nextO == -1 ) { nextO = vi[z]; }
				if ( vc[z]=='B' && nextB == -1 ) { nextB = vi[z]; }
				if ( nextO != -1 && nextB != -1 ) break;
			}

			if ( next == 'B' ) {
				dtm = abs(vi[j]-bp)+1;
				tm += dtm;
				bp=vi[j];
				if ( op < nextO ) {
					op += dtm;
					if ( op > nextO ) { op = nextO; }
				} else {
					op -= dtm;
					if ( op < nextO ) { op = nextO; }
				}
			} else if ( next == 'O' ) {
				dtm = abs(vi[j]-op)+1;
				tm += dtm;
				op=vi[j];
				if ( bp < nextB ) {
					bp += dtm;
					if ( bp > nextB ) { bp = nextB; }
				} else {
					bp -= dtm;
					if ( bp < nextB ) { bp = nextB; }
				}
			}
		}
		
		cout << "Case #" << (i+1) << ": " << tm << endl;

	}

	return 0;

}