#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define fori(i, n) for ( int i = 0; i < (n); ++i )
#define forr(i, a, b) for ( int i = (a); i <= (b); ++i )
#define ford(i, a, b) for ( int i = (a); i >= (b); --i )
#define tr(it, a, b) for ( typeof(a) it = (a); it != (b); ++it )
#define all(x) (x).begin(),(x).end()
#define sz size()
#define pb push_back

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }
template<class T> T s2a(string s) { istringstream i(s); T x; i >> x; return x; }

const double EPS = 1e-9;
const int INF = 0x3F3F3F3F;

int cmpD( double x, double y = 0, double tol = EPS )
{
    return ( x <= y + tol ) ? ( x + tol < y ) ? -1 : 0 : 1;
}

bool is_winner( const vector< string > & m, char c )
{
	int cnt;

	// lines
	fori(i,4)
	{
		cnt = 0;
		fori(j,4) if ( m[i][j] == c || m[i][j] == 'T' ) cnt++;
		if ( cnt == 4 ) return true;
	}

	// columns
	fori(j,4)
	{
		cnt = 0;
		fori(i,4) if ( m[i][j] == c || m[i][j] == 'T' ) cnt++;
		if ( cnt == 4 ) return true;
	}

	// main diagonal
	cnt = 0;
	fori(i,4) if ( m[i][i] == c || m[i][i] == 'T' ) cnt++;
	if ( cnt == 4 ) return true;

	// secondary diagonal
	cnt = 0;
	fori(i,4) if ( m[i][3-i] == c || m[i][3-i] == 'T' ) cnt++;
	if ( cnt == 4 ) return true;
}

int main()
{
	ios::sync_with_stdio(false);
	int T;
	bool full;
	string s;
	cin >> T;
	getline( cin, s );
	forr(t,1,T)
	{
		vector< string > m(4);
		full = true;
		fori(i,4)
		{
			getline( cin, m[i] );
			if ( full ) fori(j,4) if ( m[i][j] == '.' ) { full = false; break; }
		} 
		getline( cin, s );
		cout << "Case #" << t << ": ";
		if ( is_winner( m, 'X' ) ) cout << "X won" << endl;
		else if ( is_winner( m, 'O' ) ) cout << "O won" << endl;
		else if ( full ) cout << "Draw" << endl;
		else cout << "Game has not completed" << endl;
	}
    return 0;
}
