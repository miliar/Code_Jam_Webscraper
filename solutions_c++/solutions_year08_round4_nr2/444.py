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

void doIt() {
    int a, b, A;
    scanf( "%d %d %d", &a, &b, &A );
    FORD(x1,a,0-1)
        FORD(y1,b,0-1)
            FORD(x2,x1,0-1)
                FORD(y2,b,0-1) {
                    int tmp = x1*y2-x2*y1;
                    if( tmp<0 )
                        tmp = -tmp;
                    if( A==tmp ) {
                        printf("0 0 %d %d %d %d\n", x1, y1, x2, y2 );
                        return;
                    }
                   
                }
                    
    printf("IMPOSSIBLE\n");
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
