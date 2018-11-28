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



bool check( vector<string> field, int x, int y, int cnt )
{
	if ( cnt == 0 ) return true;

	char c = field[x][y];
	cnt = cnt - 1;
	int tcnt = cnt;
	int tx = x, ty = y;

	while ( tx > 0 ) {
		tx--;
		if ( field[tx][ty] == c ) tcnt--;
		else break;
		if ( tcnt <= 0 ) return true;

	}

	tcnt = cnt;
	tx = x; ty = y;
	while ( ty > 0 ) {
		ty--;
		if ( field[tx][ty] == c ) tcnt--;
		else break;
		if ( tcnt <= 0 ) return true;

	}

	tcnt = cnt;
	tx = x; ty = y;
	while ( ty < field.size() - 1 ) {
		ty++;
		if ( field[tx][ty] == c ) tcnt--;
		else break;
		if ( tcnt <= 0 ) return true;

	}

	tcnt = cnt;
	tx = x; ty = y;
	while ( tx < field.size() - 1 ) {
		tx++;
		if ( field[tx][ty] == c ) tcnt--;
		else break;
		if ( tcnt <= 0 ) return true;

	}


	tcnt = cnt;
	tx = x; ty = y;
	while ( tx < field.size() - 1 && ty < field.size() - 1 ) {
		tx++; ty++;
		if ( field[tx][ty] == c ) tcnt--;
		else break;
		if ( tcnt <= 0 ) return true;

	}

	tcnt = cnt;
	tx = x; ty = y;
	while ( tx > 0 && ty < field.size() - 1 ) {
		tx--; ty++;
		if ( field[tx][ty] == c ) tcnt--;
		else break;
		if ( tcnt <= 0 ) return true;

	}

	tcnt = cnt;
	tx = x; ty = y;
	while ( tx < field.size() - 1 && ty > 0 ) {
		tx++; ty--;
		if ( field[tx][ty] == c ) tcnt--;
		else break;
		if ( tcnt <= 0 ) return true;

	}

	tcnt = cnt;
	tx = x; ty = y;
	while ( tx > 0 && ty > 0 ) {
		tx--; ty--;
		if ( field[tx][ty] == c ) tcnt--;
		else break;
		if ( tcnt <= 0 ) return true;

	}

	return false;

}


int main ( void )
{
	vector<string> field;
	vector<string> tfield;
	string tmp;
	int t;
	int n, K;
	bool DEBUG = false;

	string ans;

	cin >> t;
	REP ( i, t ) {
		cin >> n >> K;
		field.clear();
		tfield.clear();
		
		// ボード読み込み
		REP ( k, n ) {
			cin >> tmp;
			field.PB ( tmp );
			
		}
		if ( DEBUG ) cout << "----------------" << endl;

		// Gravity
		REP ( k, n ) {
			string tmp;
			int cnt = 0;
			REP ( j, n ) {
				if ( field[k][j] != '.' ) {
					tmp = tmp + field[k][j];
			
				} else {
					cnt++;

				}
			
			}
			REP ( j, cnt ) {
				tmp = "." + tmp;

			}
			field[k] = tmp;

		}

		// ボード回転
		REP ( k, n ) {
			tmp = "";
			REP ( j, n ) {
				tmp = tmp + field[n-j-1][k];
			}
			tfield.PB ( tmp );
			if ( DEBUG ) cout << tmp << endl;

		}
		
		// check
		bool rflag = false, bflag = false;
		REP ( k, n ) {
			REP ( j, n ) {
				if ( tfield[k][j] != '.' ) {
					// R or B
					if ( tfield[k][j] == 'R' && rflag == false ) {
						if ( check( tfield, k, j, K ) == true ) {
							rflag = true;

						}

					} else if ( tfield[k][j] == 'B' && bflag == false ) {
						if ( check( tfield, k, j, K ) == true ) {
							bflag = true;

						}

					}

				}
				if ( rflag == true && bflag == true ) break;

			}
			if ( rflag == true && bflag == true ) break;

		}
		if ( rflag == true && bflag == true ) {
			cout << "Case #" << i+1 << ": Both" << endl;

		} else if ( rflag == false && bflag == false ) {
			cout << "Case #" << i+1 << ": Neither" << endl;

		} else if ( rflag == true ) {
			cout << "Case #" << i+1 << ": Red" << endl;

		} else if ( bflag == true ) {
			cout << "Case #" << i+1 << ": Blue" << endl;

		}

	}

	return 0;

}

