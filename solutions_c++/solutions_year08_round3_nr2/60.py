#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define FOR(i,a,b) for( int i=(a); i<(b); ++i)
#define FORD(i,a,b) for( int i=(a); i>(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) (int)(X).size()
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end(); ++it)


int re[4], p[4] = { 2, 3, 5, 7 };
LL d[64][2][3][5][7];

void cal( string t ){
	memset (re, 0, sizeof(re) );
	REP( i, SZ(t) )
		REP( j, 4 )
			re[j] = (re[j] * 10 + t[i]-'0') % p[j];
}

void proc( int p, int c ){
	REP( i, 2 ) REP( j, 3 ) REP( k, 5 ) REP( q, 7 ){
		d[c][ (i+re[0])%2 ][ (j+re[1])%3 ][ (k+re[2])%5 ][ (q+re[3])%7 ] += d[p][i][j][k][q];
		if( p )	d[c][ (2+i-re[0])%2 ][ (3+j-re[1])%3 ][ (5+k-re[2])%5 ][ (7+q-re[3])%7 ] += d[p][i][j][k][q];
	}
}

int main(){
	int tn;
	cin >> tn;
	int cn = 1;
	while( tn-- ){
		string s;
		cin >> s;
		int l = SZ(s);

		memset( d, 0, sizeof(d) );
		d[0][0][0][0][0] = 1;
		
		FOR( i, 1, l+1 ){
			//cout << i << endl;
			FOR( j, 1, i+1 ){
				cal ( s.substr( j-1, i-j+1 ) );
				//cout << "\t" << s.substr(j, i-j+1 ) << endl;
				//REP( k, 4 ) cout << re[k] << " / ";
				//cout << endl;
				proc( j-1, i );
			}
		}

		LL sol = 0;
		REP( i, 2 ) REP( j, 3 ) REP( k, 5 ) REP( q, 7 ){
			if( i && j && k && q ) continue;
			sol += d[l][i][j][k][q];
		}

		printf("Case #%d: %lld\n", cn++, sol);

	}
}
