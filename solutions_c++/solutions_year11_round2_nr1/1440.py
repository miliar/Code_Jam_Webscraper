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
	int t, n;
	VS tbl;
	string tmp;

	cin >> t;

	REP(i,t){
		double rpi[100];
		double wp[100];
		double owp[100];
		double oowp[100];
		int wins[100];
		int totals[100];

		cin >> n;
		tbl.clear();
		REP(j,n){
			cin >> tmp;
			tbl.PB(tmp);
		}

		// calculate wp
		REP(j,n){
			int tcnt = 0;
			int win = 0;
			REP(k,n){
				if ( tbl[j][k] != '.' ) {
					tcnt++;
					if ( tbl[j][k] == '1' ) win++;
				}
			}
			wins[j] = win;
			totals[j] = tcnt;
			wp[j] = (double)win/tcnt;
		}

		// calculate owp
		REP(j,n){
			int owpt = 0, owptcnt = 0;
			int tcn = 0;
			double twp = 0;

			REP(k,n){
				if ( j == k ) continue;
				if ( tbl[j][k] == '.' ) continue;
				tcn++;
				owpt=0; owptcnt=0;
				REP(l,n){
					if ( l == j ) continue;
					if ( tbl[k][l] == '.' ) continue;
					if ( tbl[k][l] == '1' ) {
						owpt++;
					}
					owptcnt++;
				}
				twp = twp + (double)owpt/owptcnt;
			}
			owp[j] = twp / tcn;

		}

		// calculate oowp
		REP(j,n){
			double toowp = 0;
			int tcn = 0;
			REP(k,n){
				if ( tbl[j][k] == '.' ) continue;
				toowp += owp[k];
				tcn++;
			}
			oowp[j] = (double)toowp/tcn;
		}

		// RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

		cout << "Case #" << (i+1) << ":" << endl;
		REP(j,n){
			printf("%.8f\n", (25*wp[j]+50*owp[j]+25*oowp[j])/100 );
		}

	}

	return 0;

}