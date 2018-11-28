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

#define I ((m-1)/2)

int m, v;
int d[10002][2];
int g[10002], c[10002];

int proc( int n, int v ){
	if( n > I ){
		if( v != g[n] ) return 234234234;
		else return 0;
	}
	if( d[n][v] != -1 ) return d[n][v];

	d[n][v] = 234234234;

	if( g[n] == 0 || c[n] ){ // OR
		int p = ( g[n] == 0 )?0:1;
		if( v == 1 ){
			d[n][v] = min( d[n][v], proc(2*n,0) + proc(2*n+1,1) + p );
			d[n][v] = min( d[n][v], proc(2*n,1) + proc(2*n+1,1) + p );
			d[n][v] = min( d[n][v], proc(2*n,1) + proc(2*n+1,0) + p );
		}
		else
			d[n][v] = min(d[n][v], proc(2*n,0)+proc(2*n+1,0) + p );
	}


	if( g[n] == 1 || c[n] ){ // AND
		int p = ( g[n] == 1 )?0:1;
		if( v == 0 ){
			d[n][v] = min( d[n][v], proc(2*n,0) + proc(2*n+1,1) + p );
			d[n][v] = min( d[n][v], proc(2*n,0) + proc(2*n+1,0) + p );
			d[n][v] = min( d[n][v], proc(2*n,1) + proc(2*n+1,0) + p );
		}
		else
			d[n][v] = min(d[n][v], proc(2*n,1)+proc(2*n+1,1) + p );

	}

	return d[n][v];
}

int main(){
	int tn;
	cin >> tn;
	int cn = 1;
	while(tn--){
		cin >> m >> v;
		memset( d, -1, sizeof(d) );
		memset( g, -1, sizeof(g) );
		memset( c, 0, sizeof(c) );
		REP( i, (m-1)/2 )
			cin >> g[i+1] >> c[i+1];
		FOR( i, (m-1)/2, m )
			cin >> g[i+1];

		printf("Case #%d: ", cn++);
		if( proc(1, v) == 234234234 ) cout << "IMPOSSIBLE" << endl;
		else cout << proc(1, v) << endl;
	}
}
