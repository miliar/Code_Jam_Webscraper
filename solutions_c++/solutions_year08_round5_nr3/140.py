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



#define tpow(x) (1<<(x))

int d[16][1024];
int f[16];

int bcnt( int a ){
	int re = 0;
	while( a ){
		a = (a & (a-1));
		re++;
	}
	return re;
}

int main(){

	freopen("inp.in", "r", stdin );
	freopen("out", "w", stdout );

	int tn;
	int cn = 1;
	cin >> tn;
	while(tn--){
		int n, m;
		cin >> m >> n;
		memset( d, 0, sizeof(d) );
		memset( f, 0, sizeof(f) );

		REP( i, m ){
			string s;
			cin >> s;
			REP( j, n ) if( s[j] == 'x' ) f[i] |= tpow(j);
		}

		REP( i, m ){
			REP( j, tpow(n) ){
				int ff = (f[i] | j);
				
				REP( k, tpow(n) ){
					if( k & ff ) continue;
					int fff = 0;
					REP( c, n ){
						if( k & tpow(c) ){
							if( c-1 >= 0 ) fff |= tpow(c-1);
							//fff |= tpow(c);
							if( c+1 < n ) fff |= tpow(c+1);
						}
						if( (k & tpow(c)) && (k & tpow(c+1)) ) goto no;
					}
					d[i+1][fff] = max( d[i+1][fff], d[i][j] + bcnt(k) );
no:;
				}

			}
		}
		
		int out = 0;
		REP( i, tpow(n) ){
			out = max(out, d[m][i] );
		}
		printf("Case #%d: %d\n", cn++, out );
	}

}