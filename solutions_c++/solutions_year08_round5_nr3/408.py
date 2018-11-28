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

#include <bitset>

int rows[12];
int H, W;

int count( int a ) {
    int res = 0;
    while(a) {
        res += a&1;
        a >>= 1;
    }
    return res;
}

map<int, int> cache[12];

int dp( int last, int num ) {
    if( num==H )
        return 0;
    if( cache[num].find(last)!=cache[num].end() )
        return cache[num][last];
    int taken = last|rows[num];
    int best = 0;
    FOR(i,0,(1<<W)) {
        if( (taken&i)==0 && ((i<<1)&i)==0 ) {
            //printf("check %d %d %d\n", i, taken, num );
            int cand = count(i);
            cand += dp( (i<<1)|(i>>1), num+1 ); 
            best >?= cand;
        }
    }
    //printf("check %d %d %d\n", num, taken, num );
    cache[num][last] = best;
    return best;
}


void doIt() {
    scanf( "%d %d", &H, &W );
    char S[128];
    FOR(i,0,H){
        scanf( "%s", S );
        cache[i].clear();
        rows[i] = 0;
        FOR(j,0,W)
            if( S[j]=='x' )
                rows[i] |= 1<<j;
    }

    
    printf( "%d\n", dp(0, 0) );
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
