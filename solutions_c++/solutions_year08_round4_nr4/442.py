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

const int MAX = 50000+128;
char S[MAX];
char S2[MAX];

void doIt() {
    int k;
    scanf("%d %s", &k, S);
    vector<int> perm(k);
    REP(i,k)
        perm[i] = i;

    int result = MAX;
    while( next_permutation(perm.begin(), perm.end()) ) {
        for( int i = 0 ; S[i]!=0 ; i++ ) {
            S2[i] = S[(i/k)*k+perm[i%k]];
        }
        int cand = 1;
        for( int i = 1 ; S[i]!=0 ; i++ )
            if( S2[i-1]!=S2[i] )
                cand++;
        if( cand<result ) { 
            result = cand;
            //FORE(i,perm)
              //  printf("%d: %d %s\n", i, perm[i], S2);
        }
    }
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
