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
	int r, c;
	char tile;
	string tmp;
	VS picture;
	int imp = 0;
	int cnt = 0;

	cin >> t;
	REP(i,t){
		picture.clear();
		cnt = 0;
		imp = 0;

		cin >> r >> c;
		REP(j,r){
			tmp="";
			REP(k,c){
				cin >> tile;
				tmp = tmp + (char)tile;
				if ( tile != '.' ) cnt++;
			}
			picture.PB(tmp);
		}

		if ( cnt == 0 ) {
			// not need
			cout << "Case #" << (i+1) << ":" << endl;
			REP(j,r){
				cout << picture[j] << endl;
			}
			continue;
		}

		// fillig red
		REP(j,r){
			REP(k,c){
				if ( picture[j][k] == '#' ) {
					if ( j+1 == picture.size() ) {
						imp = 1; break;
					} else if ( k + 1 == c ) { 
						imp = 1; break;
					}
					if ( picture[j+1][k] != '#' || picture[j][k+1] != '#' || picture[j+1][k+1] != '#' ) {
						// impossible
						imp = 1; break;
					} else {
						picture[j][k] = '/';
						picture[j+1][k+1] = '/';
						picture[j+1][k] = '\\';
						picture[j][k+1] = '\\';
					}
				}
			}
			if ( imp == 1 ) break;
		}

		cout << "Case #" << (i+1) << ":" << endl;
		if ( imp == 1 ) {
			cout << "Impossible" << endl;
		} else {
			REP(j,r){
				cout << picture[j] << endl;
			}
		}

	}

	return 0;

}