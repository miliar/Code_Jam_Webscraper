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

int nboard[10000][10000] = {0};


bool chkboard( int x, int y, int bs )
{
	int wb = nboard[x][y];
	REP ( i, bs ) {
		if ( wb == -1 ) return false;
		REP ( j, bs ) {
			if ( nboard[x+i][y+j] == wb ) {
				wb = !wb;
			} else {
				return false;
			}
		}
		if ( bs % 2 == 0 ) wb = !wb;
	}

	REP ( i, bs ) {
		REP ( j, bs ) {
			nboard[x+i][y+j] = -1;
		}
	}


	return true;

}

int main()
{
	int t;

	cin >> t;

	REP ( i, t ) {
		int n, m;
		vector<vector<bool>> board;
		int ans = 0;
		int ansbcnt[2048] = {0};

		cin >> n >> m;
		REP ( i, n ) {
			string tmp;
			cin >> tmp;
			vector<bool> tb;
			REP ( j, m / 4 ) {
				int nm;
				if ( tmp[j] >= 'A' && tmp[j] <= 'F' ) {
					nm = 10 + ( tmp[j] - 'A' );
				} else {
					nm = tmp[j] - '0';
				}
				REP ( k, 4 ) {
					if ( ( nm & ( 8 >> k ) ) == ( 8 >> k ) ) {
						tb.PB ( true );
					} else { tb.PB ( false ); }
				}
			}
			board.PB ( tb );

		}

		REP ( k, n ) {
			REP ( j, m ) {
				if ( board[k][j] ) nboard[k][j] = 1;
				else nboard[k][j] = 0;
//				if ( board[k][j] ) cout << "1";
//				else cout << "0";
			}
//			cout << endl;
		}

		int bs = n;
		if ( bs > m ) bs = m;

		while ( bs >= 1 ) {
			REP ( k, n ) {
				REP ( j, m ) {
					if ( j+bs > m || k+bs > n ) continue;
					if ( nboard[k][j] == -1 ) continue;
					if ( chkboard( k, j, bs ) == true ) {
						ansbcnt[bs]++;
						if ( ansbcnt[bs] == 1 ) ans++;

					//REP ( k, n ) {
					//	REP ( j, m ) {
					//		if ( nboard[k][j] == 1 ) cout << "@";
					//		else if ( nboard[k][j] == 0 ) cout << "0";
					//		else cout << " ";
					//	}
					//	cout << endl;
					//}

					//cout << "--------------" << endl;

					}

				}

			}
			bs--;

		}

		cout << "Case #" << i+1 << ": " << ans << endl;
		for ( int k = 2047; k > 0; k-- ) {
			if ( ansbcnt[k] > 0 ) {
				cout << k << " " << ansbcnt[k] << endl;
			}
		}

	}

	return 0;

}