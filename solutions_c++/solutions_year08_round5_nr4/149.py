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

int d[128][128];

int main(){

	freopen("inp.in", "r", stdin );
	freopen("out", "w", stdout );

	int tn;
	int cn = 1;
	cin >> tn;
	while(tn--){

		memset( d, 0, sizeof(d) );
		d[0][0] = 1;

		int h, w, r;
		cin >> h >> w >> r;
		REP( i, r ){
			int x, y;
			cin >> x >> y;
			d[x-1][y-1] = -1;
		}
		REP( i, h ) REP( j, w ) if( i || j ){
			if( d[i][j] == -1 ) continue;
			int a, b;
			a = b = 0;
			if( i-1 >= 0 && j-2 >= 0 ) a = max( a, d[i-1][j-2] );
			if( i-2 >= 0 && j-1 >= 0 ) b = max( b, d[i-2][j-1] );
			d[i][j] = (a + b) % 10007;
		}

		printf("Case #%d: %d\n", cn++, d[h-1][w-1] );
			
	}



}