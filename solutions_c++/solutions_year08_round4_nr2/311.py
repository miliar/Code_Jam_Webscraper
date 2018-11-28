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

int main(){
	int tn;
	int cn = 1;
	cin >> tn;
	while(tn--){
		int n, m, a;
		cin >> n >> m >> a;
		REP( x1, n+1 ) REP( y1, m+1 )
			REP( x2, n+1 ) REP( y2, m+1 ){
				if( x1 == 0 && y1 == 0 ) continue;
				if( x1 == x2 && y1 == y2 ) continue;
				if( abs(x1*y2-y1*x2) == a ){
					printf("Case #%d: 0 0 %d %d %d %d\n", cn++, x1, y1, x2, y2);
					goto yes;
				}
			}
		printf("Case #%d: IMPOSSIBLE\n", cn++);
		continue;
yes:;
	}
}
