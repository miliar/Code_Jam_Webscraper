#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#pragma warning( disable : 4244 4267 4018 )
using namespace std;

typedef vector< int > vi; typedef vector< vector< int > > vvi; typedef vector< string > vs; typedef vector< double > vd;
typedef vector< vd > vvd; typedef long long ll; typedef vector< ll > vll; typedef pair< int, int > pii;
#define all( v ) (v).begin( ), (v).end( )

struct dbg {
    dbg() : dbg_( cerr ) { dbg_.setf( ios::fixed ); dbg_.precision( 16 ); }
    //ostringstream os; dbg() : dbg_( os ) { dbg_.setf( ios::fixed ); dbg_.precision( 16 ); }
    ~dbg() { dbg_ << endl; }
    dbg & operator <<( char const * str ) { dbg_ << str << ' '; return *this; }
    template < class T > dbg & operator <<( T const & t ) { dbg_ << t << ' '; return *this; }
    template < class T, class U > dbg & operator <<( pair< T, U > const & p ) { dbg_ << '('; *this << p.first; *this << p.second; dbg_ << ") "; return *this; }
    template < class T > dbg & operator <<( vector< T > const & v ) { print( all( v ) ); return *this; }
    template < class T, int N > dbg & operator <<( T (&v)[N] ) { print( v, v + N ); return *this; }
    template < class Iter > void print( Iter p, Iter q ) { dbg_ << '{'; for ( ; p != q; ++p ) *this << *p; dbg_ << "} "; }
    template < class T > dbg & operator <<( vector< vector< T > > const & v ) { for ( int i = 0; i != v.size(); ++i ) { dbg_ << ( i ? ' ' : '{' ); print( all( v[i] ) ); dbg_ << ( i == v.size() - 1 ? "} " : "\n" ); } return *this; }
    template < class T, int N, int M > dbg & operator <<( T (&v)[N][M] ) { for ( int i = 0; i != N; ++i ) { dbg_ << ( i ? ' ' : '{' ); print( v[i], v[i] + M ); dbg_ << ( i == N - 1 ? "} " : "\n" ); } return *this; }
    ostream & dbg_;
};

std::ifstream in( "c.in" );
std::ofstream out( "c.out" );

double sector( double x, double r ) {
    double ang = acos( x / r );
    double s = r * r * ang;
    return ( s - x * sqrt( r * r - x * x ) ) / 2;
}

double calc( double x1, double x2, double r ) {
    x1 = max( x1, 0. );
    x2 = max( x2, 0. );
    x1 = min( x1, r );
    x2 = min( x2, r );
    return sector( x1, r ) - sector( x2, r );
}

void main() {
    int ntests;
    in >> ntests;
    out.precision( 10 );
    out.setf( ios::fixed );
    double pi = acos( -1. );

    for ( int ntest = 1; ntest <= ntests; ++ntest ) {
        out << "Case #" << ntest << ": ";
        double f, R, t, r, g;
        in >> f >> R >> t >> r >> g;

        double total = pi * R * R;
        R -= t + f;
        R = max( R, 0. );
        f = min( f, g / 2 );
        r += f;
        g -= 2 * f;
        double res = 0;
        for ( double x = r; x < R; x += 2 * r + g ) {
            for ( double y = r; x * x + y * y < R * R; y += 2 * r + g ) {
                if ( x + g < sqrt( R * R - y * y ) ) {
                    if ( y + g < sqrt( R * R - ( x + g ) * ( x + g ) ) )
                        res += g * g;
                    else {
                        double yy = max( y, sqrt( R * R - ( x + g ) * ( x + g ) ) );
                        double yyy = min( y + g, sqrt( R * R - x * x ) );
                        res += ( yy - y ) * g + calc( yy, yyy, R ) - ( yyy - yy ) * x;
                    }
                } else {
                    double xx = max( x, sqrt( R * R - ( y + g ) * ( y + g ) ) );
                    double xxx = min( x + g, sqrt( R * R - y * y ) );
                    res += ( xx - x ) * g + calc( xx, xxx, R ) - ( xxx - xx ) * y;
                }
            }
        }

        out << 1 - 4 * res / total << endl;
    }
}