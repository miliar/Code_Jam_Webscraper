#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define VI vector<int>
#define VS vector<string>
#define VVI vector< VI >
#define PB push_back
#define ALL(a) (a).begin(), (a).end()
#define SORT(a) sort( ALL(a) )
#define IPAIR pair<int,int>
#define VIPAIR vector< IPAIR >
#define FOR(i,b,n) for ( int i = (b); i < (n); i++ )
#define REP(i,n) FOR(i,0,n)
#define ll long long

int gcd( int a, int b )
{
    if ( b == 0 ) return a;
    return gcd( b, a % b );
}

int prime( int a, int b ) {
    int g = gcd( a, b );
    //printf( "(%d,%d) => g = %d\n", a, b, g );
    int d = 2;
    int ret = 1;
    for ( d; d * d <= g; d++ ) {
        if ( g % d == 0 )
            ret >?= d;
        while ( g % d == 0 ) g /= d;
    }
    if ( g != 1 )
        ret >?= g;
    return ret;
}

int main()
{
    int N;
    scanf( "%d", &N );
    
    for ( int prob = 1; prob <= N; prob++ ) {
        ll result = 0;
        int A, B, P;
        scanf( "%d%d%d", &A, &B, &P );
        
#if 1
        VI sets( B+10, 0 );
        for ( int i = A; i <= B; i++ )
            sets[i] = i;
        int changed = 0;
        do {
            changed = 0;
            for ( int i = A; i <= B; i++ ) {
                for ( int j = A; j <= B; j++ ) {
                    if ( sets[i] == sets[j] ) continue;
                    int pr = prime( i, j );
                    //printf( "(%d,%d) => %d\n", i, j, pr );
                    if ( pr >= P ) {
                        sets[j] = sets[i];
                        changed++;
                    }
                }
            }
        } while ( changed );
        VI count( B+10, 0 );
        for ( int i = A; i <= B; i++ ) {
            count[ sets[i] ] ++;
        }
        for ( int i = A; i <= B; i++ )
            if ( count[i] > 0 ) result++;
#endif
        
        printf( "Case #%d: %lld\n", prob, result );
    }
    
    return 0;
}
