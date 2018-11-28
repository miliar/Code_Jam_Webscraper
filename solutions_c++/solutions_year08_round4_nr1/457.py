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
#define REP(i,a) FOR(i,0,a-1)
#define FORE(i,a) REP(i,SZ(a))
#define TR(it,a) for( typeof((a).begin()) it = (a).begin() ; it!=(a).end() ; ++it )
// }}}

// basic bindings {{{
#define PB push_back
#define ST first
#define ND second
// }}}

int M, V;
const int MAX = 10000+128;
const int INF = 1000000;

int nodesA[MAX];
int nodesB[MAX];

int cache0[MAX];
int cache1[MAX];

int check0( int pos );

int check1( int pos ) {
    if( cache1[pos]!=-1 )
        return cache1[pos];
    int minn;
    if( pos<=(M-1)/2 ) {
        if( nodesA[pos]==0 ) {
            minn = min(check1(pos*2)+check0(pos*2+1),
                    check0(pos*2)+check1(pos*2+1));
            minn = min( check1(pos*2)+check1(pos*2+1), minn );
            minn = min(minn, INF);
        } else {
            minn = check1(2*pos)+check1(2*pos+1);
            if( nodesB[pos]==1 ) {
                int minn2 = min(check1(pos*2)+check0(pos*2+1),
                        check0(pos*2)+check1(pos*2+1));
                minn = min(minn2+1, minn);
            }
            minn = min(minn, INF);
        }
    } else {
        if( nodesA[pos]==1 )
            minn = 0;
        else
            minn = INF;
    }
//    printf( "1: %d %d\n", pos, minn );
//    if( minn==INF )
//        printf( "1: %d\n", pos );
    return cache1[pos] = minn;
}

int check0( int pos ) {
    if( cache0[pos]!=-1 )
        return cache0[pos];
    int minn;
//    printf( "%d %d", pos, M );
    if( pos<=(M-1)/2 ) {
        //    printf( "D: 0: %d %d %d\n", pos, check0(2*pos), check0(2*pos+1)  );
        if( nodesA[pos]==1 ) {
            minn = min(check1(pos*2)+check0(pos*2+1),
                    check0(pos*2)+check1(pos*2+1));
            minn = min( check0(pos*2)+check0(pos*2+1), minn );
            minn = min(minn, INF);
        } else {
            minn = check0(2*pos)+check0(2*pos+1);
      //      printf( "D: 0: %d %d %d\n", pos, check0(2*pos), check0(2*pos+1)  );
            if( nodesB[pos]==1 ) {
                int minn2 = min(check1(pos*2)+check0(pos*2+1),
                        check0(pos*2)+check1(pos*2+1));
                minn = min(minn2+1, minn);
            }
            minn = min(minn, INF);
        }
    } else {
        if( nodesA[pos]==0 )
            minn = 0;
        else
            minn = INF;
    }
    //printf( "0: %d %d\n", pos, minn );
    //if( minn==INF )
    //    printf( "0: %d\n", pos  );
    return cache0[pos] = minn;
}


void doIt() {
    scanf( "%d %d", &M, &V );
    int a, b;
    REP(i,M+1) {
        cache0[i+1] = cache1[i+1] = -1;
        if( i<(M-1)/2 ) {
            scanf( "%d %d", &a, &b );
            nodesA[i+1] = a;
            nodesB[i+1] = b;
        } else {
            scanf("%d", &a);
            nodesA[i+1] = a;
        }
    }

    int result;
    if(V==1)
        result = check1(1);
    else
        result = check0(1);

    if( result>=INF )
        printf("IMPOSSIBLE\n");
    else
        printf("%d\n", result);
}

int main() {
    int nTests;
    scanf( "%d", &nTests);
    REP(i,nTests+1) {
        printf( "Case #%d: ", i+1 );
		doIt();
	}
	return 0;
}
