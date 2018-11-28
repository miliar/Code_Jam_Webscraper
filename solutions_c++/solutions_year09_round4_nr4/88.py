#include <algorithm>
#include <functional>

#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>

using namespace std;

struct circle {
    int X, Y, r;

    void load() { scanf( "%d %d %d", &X, &Y, &r ); }

    friend bool operator < ( const circle &A, const circle &B ) {
        if( A.X != B.X ) return A.X < B.X;
        if( A.Y != B.Y ) return A.Y < B.Y;
        if( A.r != B.r ) return A.r < B.r;
        return false;
    }
};

int n;
vector< circle > V;

inline double get_dist( circle A, circle B ) {
    int dx = A.X-B.X;
    int dy = A.Y-B.Y;
    return sqrt( double( dx*dx + dy*dy ) );
}

double solve()
{
    if( n == 1 ) {
        return V[0].r;
    }

    if( n == 2 ) {
        return max( V[0].r, V[1].r );
    }

    if( n == 3 ) {
        double mini = 1e100;

        sort( V.begin(), V.end() );
        do {
            double tmp = max<double>( ( get_dist( V[0], V[1] ) + V[0].r + V[1].r ) / 2., V[2].r );
            if( tmp < mini ) mini = tmp;
        } while( next_permutation( V.begin(), V.end() ) );

        return mini;
    }    

    return -1;
}

int main( void )
{
    int T; scanf( "%d", &T );

    for( int counter = 0; counter < T; ++counter ) {
        scanf( "%d", &n );
        V.clear(); V.resize( n );

        for( int i = 0; i < n; ++i )
            V[i].load();
        
        printf( "Case #%d: %.5lf\n", counter+1, solve() );
    }

    return (0-0);
}
