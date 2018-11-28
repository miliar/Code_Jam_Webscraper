#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

const long long MAXN = 200;

bool rob [ MAXN ];
long long p [ MAXN ], n;
long long next [ MAXN ];
long long tmp [ MAXN ];
long long poz [  ] = { 1, 1 };

void buildNext () {
    long long i, j;
    for ( i = 0; i < n; ++ i ){
        for ( j = i + 1; j < n; ++ j ){
            if ( rob [ i ] == rob [ j ] ){
                next [ i ] = j;
                break;
            }
        }
        if ( j == n )
            next [ i ] = -1;
    }
}

long long tim;

void init () {
    tim = n = 0;
    poz [ 0 ] = poz [ 1 ] = 1;
    memset ( tmp, 0, sizeof ( tmp ) );
    memset ( next, 0, sizeof ( next ) );
    memset ( p, 0, sizeof ( p ) );
    memset ( rob, 0, sizeof ( rob ) );
}

inline long long modul ( long long x ) {
    if ( x < 0 )    x = - x;
    return x;
}
void go ( bool r, long long pos, long long ind ){
    if ( ind != -1 ){
        long long dt = modul ( poz [ r ] - pos );
        tmp [ ind ] = tim + dt;
        poz [ r ] = pos;
    }
}

long long findFirst ( bool x ){
    long long i;
    for ( i = 0; i < n; ++ i )
        if ( rob [ i ] == x )
            return i;
    return -1;
}

void solve(){
    long long i;
    buildNext();
    go ( rob [ 0 ], p [ 0 ], 0 );
    bool other = ! rob [ 0 ];
    i = findFirst ( other );
    if ( i != -1 )
        go ( other, p [ i ], i );
    for ( i = 0; i < n; ++ i ){
        tim = max ( tim, tmp [ i ] );
        tim ++;//push the button
        go ( rob [ i ], p [ next [ i ] ], next [ i ] );
    }
}

int main(){
    long long i, j, t;
    char c;
    ifstream f ( "bottrust.in" );
    ofstream g ( "bottrust.out" );
    f >> t;
    for ( j = 1; j <= t; ++ j ){
        init ();
        f >> n;
        for ( i = 0; i < n; ++ i ){
            f >> c;
            f >> p [ i ];
            if ( c == 'O' )
                rob [ i ] = 0;
            else rob [ i ] = 1;
        }
        solve();
        g << "Case #" << j << ": " << tim << endl;
    }
    return 0;
}
