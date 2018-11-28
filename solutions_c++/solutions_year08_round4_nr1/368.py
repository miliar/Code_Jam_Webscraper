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
    //ostream & dbg_; dbg() : dbg_( cerr ) { dbg_.setf( ios::fixed ); dbg_.precision( 16 ); }
    ostringstream dbg_;
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

ifstream in( "a.in" );
ofstream out( "a.out" );

int m, v;
vi val, change;

int inf = 1000000;

int calc( int v, int need ) {
    if ( v >= m / 2 )
        return need == val[v] ? 0 : -1;
    int res = inf;
    if ( val[v] || change[v] ) {
        if ( need ) {
            int l = calc( 2 * v + 1, 1 );
            int r = calc( 2 * v + 2, 1 );
            if ( l >= 0 && r >= 0 )
                res = min( res, l + r + !val[v] );
        } else {
            int l = calc( 2 * v + 1, 0 );
            int r = calc( 2 * v + 2, 0 );
            if ( l >= 0 )
                res = min( res, l + !val[v] );
            if ( r >= 0 )
                res = min( res, r + !val[v] );
        }
    }
    if ( !val[v] || change[v] ) {
        if ( need ) {
            int l = calc( 2 * v + 1, 1 );
            int r = calc( 2 * v + 2, 1 );
            if ( l >= 0 )
                res = min( res, l + val[v] );
            if ( r >= 0 )
                res = min( res, r + val[v] );
        } else {
            int l = calc( 2 * v + 1, 0 );
            int r = calc( 2 * v + 2, 0 );
            if ( l >= 0 && r >= 0 )
                res = min( res, l + r + val[v] );
        }
    }
    dbg() << v << res;
    return res;
}

void main() {
    int ntests;
    in >> ntests;
    for ( int ntest = 1; ntest <= ntests; ++ntest ) {
        out << "Case #" << ntest << ": ";
        in >> m >> v;
        val = change = vi( m );
        for ( int i = 0; i < m; ++i ) {
            if ( i < m / 2 )
                in >> val[i] >> change[i];
            else
                in >> val[i];
        }

        dbg() << val << change;
        int res = calc( 0, v );
        if ( res == inf )
            out << "IMPOSSIBLE";
        else
            out << res;
        out << endl;
    }
}