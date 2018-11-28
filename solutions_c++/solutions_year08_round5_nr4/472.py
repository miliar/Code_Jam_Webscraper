
// Jacek Migdal (jacek at migdal.pl) 2008-08-02
// basic includes {{{
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <utility>
#include <queue>
#include <cmath>
using namespace std;
// }}}

// basic types {{{
typedef char s8;
typedef short s16;
typedef int s32;
typedef long long s64;

typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;
typedef unsigned long long u64;
// }}}

// basic loops {{{
#define FOR(i,a,b) for( s32 i = (a) ; (i)<(b) ; ++(i) )
#define FORD(i,a,b) for( s32 i = (a) ; (i)>(b) ; --(i) )
#define SZ(a) (a).size()
#define REP(i,a) FOR(i,0,a)
#define FORE(i,a) REP(i,SZ(a))
#define TR(it,a) for( typeof((a).begin()) it = (a).begin() ; it!=(a).end() ; ++it )
// }}}

// basic bindings {{{
#define PB push_back
#define ST first
#define ND second
// }}}

const int MOD = 10007;
typedef pair<int,int> ii;
int DP[128][128];


int rek( int h, int w ) {
    //if( h>w ) {
     //   swap( h, w );
    //}
    if( h<=0 )
        return 0;
    int& ret = DP[h][w];
    if( ret!=-1 )
        return ret;
    
    //printf( "D: %d %d %d\n", h, w, ((rek(h-1, w-2)+rek(h-2,w-1))%MOD));
    ret = ((rek(h-1, w-2)+rek(h-2,w-1))%MOD);
    return ret;
}

int mod( int a ) {
    return (a%MOD+MOD)%MOD;
}

void doIt() {
    int H, W, R;
    scanf( "%d %d %d", &H, &W, &R );

    REP(i,128)
        REP(j,128)
            DP[i][j] = -1;
    DP[1][1] = 1;
    for( int i = 0 ; i<R ; i++ ) {
        int x, y;
        scanf("%d %d", &x, &y);
        DP[x][y] = 0;
        //result -= (rek( y, x )*rek(H-y+1, W-x+1))%MOD;
        //printf( "D: %d %d %d %d\n", rek( y, x ), rek(H-y, W-x), H-y, W-x);
    }

    int result = rek( H, W );
    result = mod(result);
    printf("%d\n", result);
}

int main() {
    int nTests;
    scanf( "%d", &nTests);
    REP(i,nTests) {
        printf( "Case #%d: ", i+1 );
		doIt();
	}
	return 0;
}
