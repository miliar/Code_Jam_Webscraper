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
    //dbg() : dbg_( cerr ) { dbg_.setf( ios::fixed ); dbg_.precision( 16 ); }
    ostringstream os; dbg() : dbg_( os ) { dbg_.setf( ios::fixed ); dbg_.precision( 16 ); }
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

template < class t > vector< t > split( string const & str )
{ istringstream iss( str ); return vector< t >( istream_iterator< t >( iss ), istream_iterator< t >( ) ); }

std::ifstream in( "b.in" );
std::ofstream out( "b.out" );

int parse( string const & s ) { 
    int h, m;
    sscanf( s.c_str(), "%d:%d", &h, &m );
    return h * 60 + m;
}

pii read_time() {
    string s;
    getline( in, s );
    vs t = split< string >( s );
    return make_pair( parse( t[0] ), parse( t[1] ) );
}

void main() {
    int ntests;
    in >> ntests;
    for ( int ntest = 1; ntest <= ntests; ++ntest ) {
        out << "Case #" << ntest << ": ";
        int turn;
        in >> turn;
        int na, nb;
        in >> na >> nb;
        vector< pii > e;
        string s; getline( in, s );
        for ( int i = 0; i < na; ++i ) {
            pii p = read_time();
            e.push_back( make_pair( p.first, 2 ) );
            e.push_back( make_pair( p.second + turn, 3 ) );
        }
        for ( int i = 0; i < nb; ++i ) {
            pii p = read_time();
            e.push_back( make_pair( p.first, 4 ) );
            e.push_back( make_pair( p.second + turn, 1 ) );
        }

        sort( all( e ) );

        dbg() << e;

        int ra, rb, cura, curb;
        ra = rb = cura = curb = 0;
        for ( int i = 0; i < e.size(); ++i ) {
            switch ( e[i].second ) {
            case 2: if ( !cura ) ++ra; else --cura; break;
            case 1: ++cura; break;
            case 4: if ( !curb ) ++rb; else --curb; break;
            case 3: ++curb; break;
            }
        }

        out << ra << " " << rb << endl;
    }
}