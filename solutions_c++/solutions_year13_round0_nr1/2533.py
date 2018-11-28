
#include <set>
#include <list>
#include <stack>
#include <cmath>
#include <queue>
#include <ctime>
#include <cfloat>
#include <vector>
#include <string>
#include <cstdio>
#include <bitset>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iomanip>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;


#define FOR(i, a, b) for(int i = a; i <= b; ++i)
#define RFOR(i, b, a) for(int i = b; i >= a; --i)
#define REP(i, N) for(int i = 0; i < N; ++i)
#define RREP(i, N) for(int i = N-1; i >= 0; --i)
#define FORIT(i, a) for( TI(a) i = a.begin(); i != a.end(); i++ )
#define MAXN 10000
#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3FFFFFFFFFLL
#define FILL(X, V) memset( X, V, sizeof(X) )
#define TI(X) __typeof((X).begin())
#define ALL(V) V.begin(), V.end()
#define SIZE(V) int((V).size())
#define pb push_back
#define mp make_pair

struct tri{
	int ant, novo;
	tri ( int ant = 0, int novo = 0) : ant(ant), novo(novo) { }
};

int n, m;
typedef vector < int > vi;
typedef vector < vi > vii;
typedef vector < tri > vtri;
typedef vector < vtri > vvtri;
typedef long long int64;
typedef unsigned long long uint64;

int x[] = {-1,-1,-1, 0, 1, 1, 1, 0 };
int y[] = {-1, 0, 1, 1, 1, 0,-1,-1 };

int main(){
	ios::sync_with_stdio(false);
	int caso = 1;
	int t;
	cin >> t;
	char mat[100][100];
	while( t-- ){
		bool x = false, o = false, cont = true;
		int qt = 0;
		REP(i,4){ 
			char *p = NULL;
			REP(j,4){
				cin >> mat[i][j];
				if( mat[i][j] == '.' ) cont = false;
			}
			p = strstr(mat[i], "XXXX");
			if( p != NULL ) x = true;
			p = strstr(mat[i], "XXXT");
			if( p != NULL ) x = true;
			p = strstr(mat[i], "TXXX");
			if( p != NULL ) x = true;
			p = strstr(mat[i], "OOOO");
			if( p != NULL ) o = true;
			p = strstr(mat[i], "OOOT");
			if( p != NULL ) o = true;
			p = strstr(mat[i], "TOOO");
			if( p != NULL ) o = true;
		}
		string str = "";
		string diaA = "";
		string diaB = "";
		REP(i,4){
			str = "";
			REP(j,4){
				str += mat[j][i];
				if ( i == j ) diaA += mat[j][i];
				if ( (i + j) == 3 ) diaB += mat[j][i];
			}
			if( str == "XXXX" || str == "XXXT" || str == "TXXX" ) x = true;
			if( str == "OOOO" || str == "OOOT" || str == "TOOO" ) o = true;
		}
		if( diaA == "XXXX" || diaA == "XXXT" || diaA == "TXXX" ) x = true;
		if( diaA == "OOOO" || diaA == "OOOT" || diaA == "TOOO" ) o = true;
		if( diaB == "OOOO" || diaB == "OOOT" || diaB == "TOOO" ) o = true;
		if( diaB == "XXXX" || diaB == "XXXT" || diaB == "TXXX" ) x = true;
		cout << "Case #" << caso++ << ": ";
		if( x && o ) cout << "Draw";
		else if( x ) cout << "X won";
		else if( o ) cout << "O won";
		else if( cont ) cout << "Draw";
		else cout << "Game has not completed";
		cout << "\n";
	}
	return 0;
}
