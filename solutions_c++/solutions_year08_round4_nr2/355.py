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
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <boost/assign.hpp>
#include <boost/tuple/tuple.hpp>
#include <boost/tuple/tuple_comparison.hpp>
#include <boost/tuple/tuple_io.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/utility.hpp>
#pragma warning( disable : 4244 4267 4018 )
using namespace std; using namespace boost; using namespace boost::assign;
typedef vector< int > vi; typedef vector< vector< int > > vvi; typedef vector< string > vs; typedef vector< double > vd;
typedef vector< vd > vvd; typedef long long ll; typedef vector< ll > vll; typedef vector< vll > vvll; typedef pair< int, int > pii;
#define all( v ) (v).begin( ), (v).end( )

struct dbg {
    ostream & dbg_; dbg() : dbg_( cerr ) { dbg_.setf( ios::fixed ); dbg_.precision( 16 ); }
    //ostringstream dbg_;
    ~dbg() { dbg_ << endl; }
    dbg & operator <<( char const * str ) { dbg_ << str << ' '; return *this; }
    template < class T > dbg & operator <<( T const & t ) { dbg_ << t << ' '; return *this; }
    template < class T, class U > dbg & operator <<( pair< T, U > const & p ) { dbg_ << '('; *this << p.first; *this << p.second; dbg_ << ") "; return *this; }
    template < class T > dbg & operator <<( vector< T > const & v ) { print( all( v ) ); return *this; }
    template < class T, int N > dbg & operator <<( T (&v)[N] ) { print( v, v + N ); return *this; }
    template < class Iter > void print( Iter p, Iter q ) { dbg_ << '{'; for ( ; p != q; ++p ) *this << *p; dbg_ << "} "; }
    template < class T > dbg & operator <<( vector< vector< T > > const & v ) { for ( int i = 0; i != v.size(); ++i ) { dbg_ << ( i ? ' ' : '{' ); print( all( v[i] ) ); dbg_ << ( i == v.size() - 1 ? "} " : "\n" ); } return *this; }
    template < class T, int N, int M > dbg & operator <<( T (&v)[N][M] ) { for ( int i = 0; i != N; ++i ) { dbg_ << ( i ? ' ' : '{' ); print( v[i], v[i] + M ); dbg_ << ( i == N - 1 ? "} " : "\n" ); } return *this; }
};

template < class T > T egcd( T a, T b, T & x, T & y ) {
    if ( b == 0 ) { x = 1; y = 0; return a; }
    T xx, yy;
    T res = egcd( b, a % b, xx, yy );
    x = yy;
    y = xx - ( a / b ) * yy;
    return res;
}

ifstream in( "b.in" );
ofstream out( "b.out" );

ll n, m;

void main() {
    int ntests;
    in >> ntests;
    ll x1 = 0, y1 = 0, x2, y2, x3, y3;
    for ( int ntest = 1; ntest <= ntests; ++ntest ) {
        out << "Case #" << ntest << ": ";
        ll n, m, a;
        in >> n >> m >> a;
        bool found = false;
        for ( y2 = 0; y2 <= m; ++y2 ) {
            for ( y3 = 0; y3 <= m; ++y3 ) {
                for ( x3 = 0; x3 <= n; ++x3 ) {
                    ll b = a + x3 * y2;
                    if ( y3 == 0 )
                        x2 = 0;
                    else
                        x2 = b / y3;
                    if ( x2 <= n && x2 * y3 - x3 * y2 == a ) {
                        found = true;
                        goto found;
                    }
                }
                //ll g = egcd( y3, y2, x2, x3 );
                //ll t = a / g;
                //if ( a - t * g != 0 ) continue;
                //x2 *= t; x3 *= -t;
                //if ( x2 >= 0 && x3 >= 0 && x2 <= n && x3 <= n ) {
                //    assert( x1 * y2 - x2 * y1 + x2 * y3 - x3 * y2 + x3 * y1 - x1 * y3 == a );
                //    found = true;
                //    goto found;
                //}
            }
        }

found:  
        if ( !found )
            out << "IMPOSSIBLE";
        else
            out << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3;
        out << endl;
    }
}