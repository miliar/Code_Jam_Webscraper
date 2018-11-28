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

int p, k, l;
int d[1024];

int main(){
	int tn;
	cin >> tn;
	int cn = 1;
	while(tn--){
		LL sol = 0;
		cin >> p >> k >> l;
		REP( i, l ) cin >> d[i];

		sort( d, d+l );
		reverse( d, d+l );

		int j = k; int v = 1;
		REP( i, l ){
			j--;
			sol += (LL)v * d[i];
			if( j == 0 ) j = k, v++;
		}

		printf("Case #%d: %lld\n", cn++, sol);
	}
}
